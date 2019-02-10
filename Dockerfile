FROM jjanzic/docker-python3-opencv
LABEL maintainer "Chuck Bassett <chucksmash@users.noreply.github.com>"

RUN mkdir -p /opt/frame-finder

RUN pip install --upgrade pip
COPY ./requirements.txt /opt/frame-finder/requirements.txt
RUN pip install -r /opt/frame-finder/requirements.txt

COPY ./python /opt/frame-finder
COPY ./README.md /opt/frame-finder
WORKDIR /opt/frame-finder
RUN python3.7 setup.py install
