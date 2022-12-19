FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /zoobiblioarch
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . /zoobiblioarch/



