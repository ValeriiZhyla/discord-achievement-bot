# syntax=docker/dockerfile:1

FROM python:3.11-slim
ARG DISCORD_BOT_TOKEN
ARG CHANNEL_ID

ENV DISCORD_BOT_TOKEN=$DISCORD_BOT_TOKEN
ENV PG_PASSWORD=$PG_PASSWORD

WORKDIR /discord-bot-app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "bot.py", "--host=0.0.0.0"]

