
second_dir = []

file_tree = {}
with open('config.yaml', 'r') as ymlfile:
    dirs = ymlfile.readlines()
    print(dirs)

    for v in dirs:
        v.replace(':/n', '')
        if v.startswith('- '):
            root_dir = v.strip('- ')[:-2]
            print(root_dir)
            file_tree.update({root_dir: {}})
            print(file_tree)
        if v.startswith('  -'):
            v = v.strip('- ')[:-2]
            file_tree[root_dir].update({v: []})
        if not v.endswith(':'):
            file_tree[v].append(v)

            print(file_tree)
