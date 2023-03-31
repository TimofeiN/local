import os


clear_list = []
root_dir = ''
with open('config.yaml', 'r') as ymlfile:
    for line in ymlfile:
        print(line)
        if line.startswith('- '):
            root_dir = line.strip('- ')[:-2]
            print(root_dir)
