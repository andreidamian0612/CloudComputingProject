import zipfile
import os

homework_file = 'tema3'
workspace = "homework"
checker_script = ''
from_master = 'path'

def start_worker(foldername):
    student_name = foldername.split('_')[0]
    print(foldername)
    for file in os.listdir(foldername):
        if file.endswith('.zip'):
            with zipfile.ZipFile(os.path.join(foldername, file), 'r') as zip_ref:
                zip_ref.extractall(workspace)
    os.chdir(workspace)
    os.system('make')
    os.system(checker_script)

if __name__ == '__main__':
    start_worker(foldername=)