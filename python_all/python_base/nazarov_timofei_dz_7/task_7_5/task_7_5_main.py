import os
import json

os.chdir('some_data')
root_dir = os.path.abspath(os.curdir)

limits = [10**n for n in range(2, 6)]
stat_dict = {el: {} for el in limits}
tmp = [[] for i in range(len(limits))]
n = 0

for path, dirs, files in os.walk(root_dir):
    for file in files:
        size = os.stat(f'{path}/{file}').st_size
        if size <= limits[n]:
            tmp[n].append(file)
        elif limits[n] < size <= limits[n+1]:
            tmp[n+1].append(file)
        elif limits[n+1] < size <= limits[n+2]:
            tmp[n+2].append(file)
        else:
            tmp[n+3].append(file)

for el in tmp:
    exts = {file.rsplit('.', maxsplit=1)[-1].lower() for file in el}
    stat_dict.update({limits[n]: (len(el), list(exts))})
    n = n + 1
print(stat_dict)

os.chdir('../')
with open('some_data_summary.json', 'w', encoding='utf-8') as f:
    json.dump(stat_dict, f)
