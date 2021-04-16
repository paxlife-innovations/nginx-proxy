FROM python:3.7-alpine
LABEL maintainer="tan@paxlife.aero"

RUN apk add --no-cache gcc musl-dev python3-dev libffi-dev openssl-dev && \
    pip install --no-cache-dir flask cryptography==2.1.4 && \
    apk del libressl-dev musl-dev libffi-dev

COPY ./app.py /app/

WORKDIR /app
ENTRYPOINT ["python3", "app.py"]
