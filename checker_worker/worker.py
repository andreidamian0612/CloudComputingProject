import zipfile
import os
import subprocess
import database as db
from time import sleep

home_path = '/home/worker'
worker_path = '/home/worker/work'
checker_environment = '/usr/src/worker/checker_environment/*'
workspace = "/home/worker/workspace"
checker_script = './checker_test.sh'

folders = []
def start_worker():
    hw_folder = os.listdir(worker_path)[0]
    hw_folder_path = os.path.join(worker_path, hw_folder)
    print(hw_folder)
    student_name = hw_folder.split('_')[0]
    print(student_name)
    print(os.listdir(hw_folder_path))
    for archive in os.listdir(hw_folder_path):
        hw_archive = os.path.join(hw_folder_path, archive)
        print(hw_archive)
        if hw_archive.endswith('.zip'):
            os.makedirs(workspace)
            os.system(f'unzip "{hw_archive}" -d {workspace}')
            break
        else:
            os.system(f'rm -rf "{hw_folder_path}"')
            return student_name, 0

    print('executing : f"cp -r {checker_environment} {workspace}"')
    os.system(f"cp -r {checker_environment} {workspace}")

    os.chdir(workspace)
    os.system('make')

    result = subprocess.check_output(checker_script).decode()

    print(result)

    success = float(result.split('\n')[0])
    fail = float(result.split('\n')[1])
    percentage = success / fail * 100

    os.chdir(home_path)

    os.system(f'rm -rf "{hw_folder_path}"')
    os.system(f'rm -rf "{workspace}"')

    return student_name, percentage


if __name__ == '__main__':
    os.system(f'rm -rf "{worker_path}/*"')
    i = 0
    # sleep(40)
    while True:
        try:
            db.init_connection()
            break
        except Exception as e:
            if i >= 5:
                raise Exception("Could not connect to database")
            i += 1
            print('Got the exception ==> wait for 15s until retry')
            print(e)
            sleep(15)
    while True:
        if len(os.listdir(worker_path)) == 0:
            sleep(1)
        else:
            student_name, percentage = start_worker()
            db.db_add_result(student_name, percentage)
