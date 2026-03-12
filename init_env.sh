#!/bin/bash

pip install torch==2.7.0 torchvision==0.22.0 torchaudio==2.7.0 --index-url https://download.pytorch.org/whl/cu128

cd s3prl
pip install .
cd ..

# Get compatible version of huggingface
pip uninstall huggingface-hub
pip install huggingface-hub==0.34.3

# Same for transformers
pip uninstall transformers
pip install transformers==4.52.4

pip install tensorboardX
pip install pandas
pip install flashlight-text

cd kenlm
pip install .
cd ..

cd sequence 
pip install .
cd ..
