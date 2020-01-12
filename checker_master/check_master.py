import subprocess
import zipfile
import os
from time import sleep
from database import db_init

upload_path = '/usr/upload'
worker_path = '/usr/upload'

def wait_work():
    while True:
        if os.listdir(upload_path).count == 0:
            sleep(1)
        else:
            start_work()

def start_work():
    for archive in os.listdir(upload_path):
        if not archive.endswith('.zip'):
            os.remove(archive.path)

        extracted_directory = os.fsencode('.'.join(archive.split('.')[:-1]))
        with zipfile.ZipFile(archive, 'r') as zip_ref:
            zip_ref.extractall(extracted_directory)

        for folder in os.listdir(extracted_directory):
            homework_folder = os.fsdecode(folder)
            start_worker(os.path.join(extracted_directory, homework_folder))

def start_worker(homework_path):
    os.rename(homework_path, os.path.join(worker_path, os.path.basename(homework_path))

if __name__ == "__main__":
    db_init()
    wait_work()
