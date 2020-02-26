FROM python:3.8.1-buster

COPY . /app
WORKDIR /app
#RUN apt-get update -y && \
#    apt-get install -y python-pip python-dev

RUN pip install -r requirements.txt


ENV LOG_LEVEL="INFO"

CMD ["python", "run.py" ]
