FROM ubuntu

RUN apt-get update
RUN apt-get -y install python3 python3-pip default-libmysqlclient-dev

COPY requirements.txt /usr/src/checker/
RUN pip3 install --no-cache-dir -r /usr/src/checker/requirements.txt

RUN mkdir -p /usr/src/checker

COPY check_master.py /usr/src/checker/
COPY database.py /usr/src/checker/

WORKDIR /usr/src/checker

CMD [ "python3", "check_master.py" ]