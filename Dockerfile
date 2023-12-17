FROM python:3.10.6


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/improve_your_file

COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt

COPY . /usr/src/improve_your_file




