FROM ubuntu

RUN apt-get update
RUN apt-get -y install python3 python3-pip default-libmysqlclient-dev

RUN mkdir -p /usr/src/checker

COPY check_master /usr/src/checker/
COPY ../database/database.py /usr/src/checker/
COPY requirements.txt /usr/src/checker/
RUN pip3 install --no-cache-dir -r /usr/src/app/requirements.txt

CMD [ "python3", "check_master.py" ]