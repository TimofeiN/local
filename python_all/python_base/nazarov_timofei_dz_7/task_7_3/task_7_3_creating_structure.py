import os
from pathlib import Path

cur_dir = os.path.abspath(os.curdir)

p = Path(f'{cur_dir}/myproject/mainapp/templates/mainapp')
if not os.path.exists(p):
    p.mkdir(parents=True, exist_ok=True)
p_1 = Path(f'{cur_dir}/myproject/authapp/templates/authapp')
if not os.path.exists(p_1):
    p_1.mkdir(parents=True, exist_ok=True)

os.chdir('myproject')
dir_path = os.path.join('settings')
if not os.path.exists(dir_path):
    os.mkdir(dir_path)

settings_files = ['__init.py__', 'dev.py', 'prod.py']
main_auth_files = ['__init.py__', 'models.py', 'views.py']
temp_files = ['base.html', 'index.html']

for file in settings_files:
    with open(f'settings/{file}', 'a') as f:
        pass

for file in main_auth_files:
    with open(f'mainapp/{file}', 'a'):
        pass
    with open(f'authapp/{file}', 'a'):
        pass

for file in temp_files:
    with open(f'authapp/templates/authapp/{file}', 'a'):
        pass
    with open(f'mainapp/templates/mainapp/{file}', 'a'):
        pass
