FROM ubuntu

# config
RUN mkdir -p /config
ADD requirements.txt /config

## setup python3
RUN set -x \
  && apt-get update \
  && apt-get install -y python3 python3-pip python3-dev \
  && apt-get install -y libsm6 libxrender1 libfontconfig1 libxext6 libglib2.0-0 \
  && apt-get install -y nano \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install -r /config/requirements.txt \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

##
RUN mkdir -p /workspace
ENV HOME /workspace
WORKDIR /workspace

CMD ["python3", "train.py"]
