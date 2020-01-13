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
    hw_folder = os.listdir(worker_path)[0]
    hw_folder_path = os.path.join(worker_path, hw_folder)
    print(hw_folder)
    student_name = hw_folder.split('_')[0]
    print(student_name)

    for archive in os.listdir(hw_folder_path):
        hw_archive = os.path.join(hw_folder_path, archive)
        print(hw_archive)
        if hw_archive.endswith('.zip'):
            os.makedirs(workspace)
            os.system(f'unzip "{hw_archive}" -d {workspace}')
        else:
            os.system(f"rm -rf {hw_folder_path}")
            return student_name, 0

    os.system(f"cp -r {checker_environment} {workspace}")

    os.chdir(workspace)
    os.system('make')

    result = subprocess.check_output(checker_script).decode()

    print(result)

    success = float(result.split('\n')[0])
    fail = float(result.split('\n')[1])
    percentage = success/fail * 100

    os.system(f"rm -rf {hw_folder}")
    os.system(f"rm -rf {workspace}")

    return student_name, percentage

if __name__ == '__main__':
    db.init_connection()
    while True:
        if len(os.listdir(worker_path)) == 0:
            sleep(1)
        else:
            student_name, percentage = start_worker()
            db.db_add_result(student_name, percentage)

