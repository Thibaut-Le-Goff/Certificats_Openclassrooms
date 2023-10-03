
FROM python:3.9.18-bookworm

RUN apt-get update -y
    #apt-get install -y python3 && \
    #apt-get install -y python3-pip 
    # pip
RUN pip3 install --upgrade pip && \
    pip3 install tensorflow && \
    pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu && \
    pip3 install nltk scikit-learn transformers vaderSentiment textblob seaborn panda regex && \
    # others commands
    useradd -ms /bin/bash user && \
    apt-get clean 

COPY entrees.py /home/user/
COPY main.py /home/user/

USER user
WORKDIR /home/user

CMD ["bash"]

# doc to install the nvidia container-toolkit :
# https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html

# Commands to run :
# docker build virtual_env
# docker run --runtime=nvidia --gpus all -it --name virtual_env1 virtual_env

