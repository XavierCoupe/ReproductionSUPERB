from collections import OrderedDict
from typing import Dict, List, Union

import torch
import torch.nn as nn

from torch.nn.parallel import DistributedDataParallel as DDP
from torch import Tensor
from torch.nn.utils.rnn import pad_sequence
from .dicehubert import HubertDiscrete




class UpstreamExpert(nn.Module):
    def __init__(self, ckpt: str = None, model_config: str = None, **kwargs):
        """
        Args:
            ckpt:
                The checkpoint path for loading your pretrained weights.
                Can be assigned by the -k option in run_downstream.py

            model_config:
                The config path for constructing your model.
                Might not needed if you also save that in your checkpoint file.
                Can be assigned by the -g option in run_downstream.py
        """
        super().__init__()
        self.name = "[DiceHubert UpstreamExpert]"

        self.checkpoint = torch.load(ckpt)
        
        self.model = HubertDiscrete(100)

        # Les params commencent par "module.", du à l'utilisation de DistributedDataParaller. Il faut les retirer
        state_dict = self.checkpoint["hubert"]
        if all(param.startswith("module.") for param in state_dict.keys()):
            state_dict = {k[len("module."):]: v for k, v in state_dict.items()}
        
        self.model.load_state_dict(state_dict)

    def get_downsample_rates(self, key: str) -> int:
        """
        Since we do not do any downsampling in this example upstream
        All keys' corresponding representations have downsample rate of 1
        """
        return 320

    def forward(self, wavs: List[Tensor]) -> Dict[str, Union[Tensor, List[Tensor]]]:
        """
        When the returning Dict contains the List with more than one Tensor,
        those Tensors should be in the same shape to train a weighted-sum on them.
        """

        wavs = pad_sequence(wavs, batch_first=True).unsqueeze(-1)
        # wavs: (batch_size, max_len, 1)

        wavs = torch.transpose(wavs, 1, 2)
        # wavs: (batch_size, 1, max_len)

        
        logits, hidden_states, mask = self.model(wavs)
        
        # The "hidden_states" key will be used as default in many cases
        # Others keys in this example are presented for SUPERB Challenge
        return {
            "logits": logits, 
            "hidden_states": hidden_states, 
            "mask": mask
        }