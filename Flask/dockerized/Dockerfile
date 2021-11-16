FROM python:3.8-slim
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
COPY . /app
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
#ENTRYPOINT ['python']
COPY . .
CMD ['app.py']
