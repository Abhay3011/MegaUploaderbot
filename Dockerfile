FROM python:3.11.1-buster

WORKDIR . .
COPY . .

RUN apt update && apt upgrade -y
RUN apt install git python3-pip -y
RUN git clone https://github.com/Abhay3011/MegaUploaderbot
WORKDIR /MegaUploaderbot
RUN pip3 install -U -r requirements.txt
CMD python3 bot.py
