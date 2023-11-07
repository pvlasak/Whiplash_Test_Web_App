FROM python:3.8.18-alpine

RUN pip install --upgrade pip

WORKDIR /flask-web-app

ADD . /flask-web-app

RUN pip install -r requirements.txt
RUN python3 config_db.py

CMD ["python3", "app.py"]

