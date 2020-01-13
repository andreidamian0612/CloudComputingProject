FROM ubuntu

RUN apt-get update
RUN apt-get -y install python3 python3-pip default-libmysqlclient-dev zip libopenmpi-dev openmpi-bin openmpi-doc openmpi-common ssh

COPY requirements.txt /usr/src/worker/
RUN pip3 install --no-cache-dir -r /usr/src/worker/requirements.txt

#for checker -- hardcoded
RUN pip3 install pillow

RUN mkdir -p /usr/src/worker

COPY checker_environment /usr/src/worker/checker_environment
COPY worker.py /usr/src/worker/
COPY database.py /usr/src/worker/

WORKDIR /usr/src/worker
RUN useradd -ms /bin/bash worker
RUN chmod 777 /usr/src/worker/checker_environment/checker_test.sh
RUN chown -R worker /usr/src/worker/

USER worker

CMD [ "python3", "worker.py" ]
