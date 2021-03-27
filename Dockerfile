FROM python:3.9-alpine

ADD ./requirements.txt .
RUN python3 -m pip install -r requirements.txt
ADD ./main.py .

ENTRYPOINT ./main.py
