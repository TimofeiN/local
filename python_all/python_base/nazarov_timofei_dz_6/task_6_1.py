import urllib.request

url = 'https://gbcdn.mrgcdn.ru/uploads/asset/2729331/attachment/e84f9ad49c706008fba3b58e2a1e5b09.txt'
data_list = []

with urllib.request.urlopen(url) as response:
    for line in response:
        line_s = line.decode('utf-8')
        line_lst = line_s.split(' ')
        data = (line_lst[0], line_lst[5][1:], line_lst[6])
        data_list.append(data)

print(data_list)
