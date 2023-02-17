FROM python:3.10.9-buster

ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND="noninteractive"

WORKDIR /usr/local/src/cti

COPY ./requirements.txt /usr/local/src/cti

RUN python3 -m pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["python", "main.py"]