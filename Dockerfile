# syntax=docker/dockerfile:1

FROM python:3.12.10-alpine3.21

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "sh", "run.sh" ]