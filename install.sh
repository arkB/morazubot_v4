#!/bin/bash

sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install libjpeg-dev libopenblas-dev libopenmpi-dev libomp-dev git-lfs -y
sudo apt autoremove -y

python -m venv v4env
source v4env/bin/activate

pip install setuptools==58.3.0
pip install Cython==0.29.33
pip install gdown==4.6.4
gdown https://drive.google.com/uc?id=1uLkZzUdx3LiJC-Sy_ofTACfHgFprumSg
pip install torch-1.13.0a0+git7c98e70-cp39-cp39-linux_aarch64.whl
rm torch-1.13.0a0+git7c98e70-cp39-cp39-linux_aarch64.whl
git clone https://github.com/huggingface/transformers -b v4.23.1
pip install transformers==4.23.1
pip install evaluate==0.3.0
pip install sentencepiece==0.1.97
pip install twitter==1.19.6
pip install python-dotenv==0.21.1

cd output/
gdown https://drive.google.com/uc?id=1vjRCyk_GSFyoU0F-ma4JfcS1_SHKBtgf
