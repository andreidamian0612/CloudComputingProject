import zipfile
import os
import subprocess
import database as db


upload_path = '/usr/upload'
worker_path = '/usr/worker'
checker_environment = '/usr/src/worker/checker_environment'

homework_file = 'tema3'
workspace = "homework"
checker_script = ''
from_master = 'path'

def start_worker(foldername):
    os.system("cp -r /usr/src/worker/checker_environment")
    student_name = foldername.split('_')[0]
    for file in os.listdir(foldername):
        if file.endswith('.zip'):
            with zipfile.ZipFile(os.path.join(foldername, file), 'r') as zip_ref:
                zip_ref.extractall(workspace)
    os.chdir(workspace)
    os.system('make')
    os.system(checker_script)
    result = subprocess.check_output('./' + checker_script).decode()
    success = float(result.split('\n')[0])
    fail = float(result.split('\n')[1])
    percentage = success/fail * 100
    return student_name, percentage

if __name__ == '__main__':
    db.init_connection()
    while True:
        if os.listdir(worker_path).count() != 0:
            student_name, percentage = start_worker(worker_path)
            db.db_add_result(student_name, percentage)
        else:
            continue

