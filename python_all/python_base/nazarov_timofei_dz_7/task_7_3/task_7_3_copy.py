import os
import shutil

os.chdir('myproject')
dir_ = os.path.abspath(os.curdir)

for path, dirs, files in os.walk(dir_):
    if path.endswith('templates'):
        print(path)
        shutil.copytree(path, f'{dir_}/templates', dirs_exist_ok=True)
