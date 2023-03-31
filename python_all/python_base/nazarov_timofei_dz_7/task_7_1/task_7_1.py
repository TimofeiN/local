# --settings --mainapp --adminapp --authapp
import os

dir_names = ['settings', 'mainapp', 'adminapp', 'authapp']

dir_path = os.path.join('my_project')
if not os.path.exists(dir_path):
    os.mkdir(dir_path)

os.chdir('my_project')
for name in dir_names:
    dir_path = os.path.join(name)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
