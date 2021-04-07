FROM raspbian/stretch as base

RUN apt update \
    && apt install -y curl
    # snap non supporté sur Docker
    #&& apt install -y snapd

ENTRYPOINT [ "/bin/bash" ]