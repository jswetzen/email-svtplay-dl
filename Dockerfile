FROM python:latest
LABEL maintainer=jswetzen

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      ffmpeg zip fetchmail && \
    rm -rf /var/lib/apt/lists/*
RUN pip install cryptography pyyaml requests
RUN git clone https://github.com/spaam/svtplay-dl.git && \
    cd svtplay-dl && \
    make && \
    make install && \
    cd .. && \
    rm -r svtplay-dl

COPY mailtrigger.sh /bin/mailtrigger
COPY run.sh /run.sh

WORKDIR /data

ENV POLL_INTERVAL 300
ENV FETCHMAIL_DEF "poll mail.example.com proto pop3 port 110 user mail@example.com password pass"
ENV DL_OPTIONS "-S --all-subtitles"

CMD /run.sh
