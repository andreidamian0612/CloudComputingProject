import zipfile
import os
import subprocess
import database as db
from time import sleep

upload_path = '/usr/upload'
worker_path = '/usr/worker'
checker_environment = '/usr/src/worker/checker_environment/*'
workspace = "/usr/workspace"
checker_script = './checker_test.sh'

def start_worker():
    hw_folder = os.path.join(worker_path, os.listdir(worker_path)[0])
    student_name = hw_folder.split('_')[0]

    for archive in os.listdir(hw_folder):
        hw_archive = os.path.join(hw_folder)
        if archive.endswith('.zip'):
            os.makedirs(workspace)
            with zipfile.ZipFile(hw_archive, 'r') as zip_ref:
                zip_ref.extractall(workspace)
        else:
            os.removedirs(hw_folder)
            return student_name, 0

    os.system(f"cp -r {checker_environment} {workspace}")

    os.chdir(workspace)
    os.system('make')

    result = subprocess.check_output(checker_script).decode()

    success = float(result.split('\n')[0])
    fail = float(result.split('\n')[1])
    percentage = success/fail * 100

    os.removedirs(hw_folder)
    os.removedirs(workspace)

    return student_name, percentage

if __name__ == '__main__':
    db.init_connection()
    while True:
        if len(os.listdir(worker_path)) == 0:
            sleep(1)
        else:
            student_name, percentage = start_worker()
            db.db_add_result(student_name, percentage)

