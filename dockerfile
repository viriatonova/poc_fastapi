FROM python:3.11-buster

ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND="noninteractive"

WORKDIR /usr/local/src/cronos_api

COPY ./requirements.txt /usr/local/src/cronos_api

RUN python3 -m pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["python", "main.py"]