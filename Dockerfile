FROM jjanzic/docker-python3-opencv
LABEL maintainer "Chuck Bassett <chucksmash@users.noreply.github.com>"

RUN mkdir -p /opt/seek_frame/{bin,seek_frame}
RUN mkdir -p /opt/data

RUN pip install --upgrade pip
COPY ./requirements.txt /opt/seek_frame/requirements.txt
RUN pip install -r /opt/seek_frame/requirements.txt

COPY ./python/data /opt/data
COPY ./python/setup.py /opt/seek_frame/setup.py
COPY ./README.md /opt/seek_frame
COPY ./python/seek_frame/ /opt/seek_frame/seek_frame/
COPY ./python/bin /opt/seek_frame/bin
WORKDIR /opt/seek_frame
RUN python3.7 setup.py install
