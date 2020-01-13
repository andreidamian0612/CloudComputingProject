import subprocess
import zipfile
import os
from time import sleep
from database import db_init

upload_path = '/usr/upload'
worker_path = '/usr/worker'
extract_to = '/usr/workspace'


def wait_work():
    while True:
        if len(os.listdir(upload_path)) == 0:
            sleep(1)
        else:
            start_work()


def start_work():
    print(os.listdir(upload_path))
    for archive in os.listdir(upload_path):
        archive_path = os.path.join(upload_path, archive)
        print (archive_path)
        if not archive.endswith('.zip'):
            os.system(f"rm -rf {archive_path}")
            continue

        os.system(f"unzip {archive_path} -d {extract_to}")
        os.system(f"mv {extract_to}/* {worker_path}")
        os.system(f"rm -rf {archive_path}")


if __name__ == "__main__":
    db_init()
    wait_work()
