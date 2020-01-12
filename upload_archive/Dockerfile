FROM ubuntu

RUN apt-get update
RUN apt-get -y install python3
RUN apt-get -y install python3-pip

COPY requirements.txt /usr/src/app/
RUN pip3 install --no-cache-dir -r /usr/src/app/requirements.txt

COPY app.py /usr/src/app/

EXPOSE 5000

CMD ["python3", "/usr/src/app/app.py"]