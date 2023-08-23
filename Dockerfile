FROM ubuntu:18.04

WORKDIR /app/

RUN apt update && \
    apt install --no-install-recommends -y --fix-missing \
    apt-utils build-essential git vim swig libatlas-base-dev libopenblas-dev

## install python 3.8
RUN apt-get install --no-install-recommends -y --fix-missing \
    python3.8 python3-pip python3.8-dev python3-setuptools python3-wheel

RUN git clone https://github.com/barbarabenato/linking_ds_vs_cp_proj.git

RUN ln -s /usr/bin/python3.8 /usr/bin/python

RUN python -m pip install wheel cython==0.29.32 numpy==1.23.2

RUN python -m pip install --upgrade pip==22.2.2

RUN cd /app/linking_ds_vs_cp_proj/ && python -m pip install dist/pyift-0.1-cp38-cp38-linux_x86_64.whl