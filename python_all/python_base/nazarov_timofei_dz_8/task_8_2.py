import re
import urllib.request


RE_DATA = re.compile(r'^([\d.]+)[\s-]+([\S\w\s]+[]])\W+(\w+)\s(\S+)\s\S+\s(\d+)\s(\d+)')

test_url = 'https://gbcdn.mrgcdn.ru/uploads/asset/2729331/attachment/e84f9ad49c706008fba3b58e2a1e5b09.txt'


def log_parsing(url):
    with urllib.request.urlopen(url) as response:
        for line in response:
            line = str(line).strip("b'")[:-3]
            print(line)
            parsed_line = RE_DATA.findall(line)
            return parsed_line


for i in range(10):
    print(log_parsing(test_url))
