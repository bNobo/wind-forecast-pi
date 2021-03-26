FROM raspbian/stretch

RUN apt update && apt install -y curl

ENTRYPOINT [ "/bin/bash" ]