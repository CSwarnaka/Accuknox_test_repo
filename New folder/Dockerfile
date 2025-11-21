FROM ubuntu:14.04

RUN apt-get update && apt-get install -y python python-pip
COPY . /app
WORKDIR /app

RUN pip install -r vulnerable_app/requirements.txt
CMD ["python", "vulnerable_app/app.py"]
