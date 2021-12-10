FROM python:3.8-slim
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
COPY . /app
WORKDIR /app
COPY . .
#COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
CMD [ "python", "app.py" ]
