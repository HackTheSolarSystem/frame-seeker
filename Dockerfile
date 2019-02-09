FROM jjanzic/docker-python3-opencv
LABEL maintainer "Chuck Bassett <chucksmash@users.noreply.github.com>"

RUN mkdir -p /opt/frame-finder

COPY ./requirements.txt /opt/frame-finder/requirements.txt
RUN pip install -r /opt/frame-finder/requirements.txt
