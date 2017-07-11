FROM python:3

WORKDIR /usr/src

COPY ask /usr/src
COPY ask/wait-for-it.sh /usr/src/

RUN pip install pymysql
RUN pip install django
RUN pip install gunicorn
RUN apt-get update
RUN apt-get install mysql-client -y
RUN apt-get clean

EXPOSE 8000