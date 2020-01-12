import subprocess
import zipfile
import os

homework_file = 'tema3'
workspace = "homework"
checker_script = 'my_script.sh'


def start_worker(foldername):
    student_name = foldername.split('_')[0]
    # print(foldername)
    for file in os.listdir(foldername):
        if file.endswith('.zip'):
            with zipfile.ZipFile(os.path.join(foldername, file), 'r') as zip_ref:
                zip_ref.extractall(workspace)
    # os.chdir(workspace)
    os.system('make')
    print(os.getcwd())
    result = subprocess.check_output('./' + checker_script).decode()
    success = result.split('\n')[0]
    fail = result.split('\n')[1]
    print(success, fail)



known_archives = []

zip_file_path = 'apd_homework.zip'
extract_to = zip_file_path + "_unzipped"
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to)

directory = os.fsencode(extract_to)
for file in os.listdir(directory):
    foldername = os.fsdecode(file)
    start_worker(os.path.join(extract_to, foldername))
    break
