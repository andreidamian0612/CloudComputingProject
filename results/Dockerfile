FROM ubuntu

RUN apt-get update
RUN apt-get -y install python3 python3-pip default-libmysqlclient-dev zip

COPY requirements.txt /root
RUN pip3 install --no-cache-dir -r /root/requirements.txt

COPY app.py /root
COPY database.py /root
COPY results.html /root/templates/

WORKDIR /root
EXPOSE 4000

CMD [ "python3", "app.py" ]