FROM ubuntu

RUN apt-get update
RUN apt-get -y install python3 python3-pip default-libmysqlclient-dev

RUN mkdir -p /usr/src/worker

COPY worker.py /usr/src/worker/
COPY checker_environment /usr/src/worker/checker_environment
COPY database.py /usr/src/worker/
COPY requirements.txt /usr/src/worker/
RUN pip3 install --no-cache-dir -r /usr/src/worker/requirements.txt

CMD [ "python3", "worker.py" ]
