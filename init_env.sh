#!/bin/bash

pip install torch==2.7.0 torchvision==0.22.0 torchaudio==2.7.0 --index-url https://download.pytorch.org/whl/cu128

# Install s3prl
pip install .
cd ..

# Get compatible version of huggingface
pip uninstall huggingface-hub
pip install huggingface-hub==0.34.3

# Same for transformers
pip uninstall transformers
pip install transformers==4.52.4

pip install tensorboardX==2.6.4
pip install pandas==2.3.3
pip install flashlight-text==0.0.7
pip install editdistance==0.8.1
pip install joblib==1.5.3
pip install catalyst==20.8.2
pip install librosa==0.11.0
pip install sox==1.5.0
pip install h5py==3.16.0

git clone https://github.com/kpu/kenlm
cd kenlm
pip install .
cd ..

git clone https://github.com/flashlight/sequence.git
cd sequence 
pip install .
cd ..

git clone https://github.com/s3prl/LibriMix.git
