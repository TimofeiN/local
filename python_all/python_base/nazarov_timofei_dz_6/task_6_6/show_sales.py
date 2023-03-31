import sys


def output_line(text):
    text = text.replace('\n', ' ')
    print(text)


n = 0
with open('bakery.csv', 'r', encoding='utf-8') as f:
    for line in f:
        n = n + 1
        if len(sys.argv) == 3:
            if int(sys.argv[1]) <= n <= int(sys.argv[2]):
                output_line(line)
        elif len(sys.argv) == 2:
            if n >= int(sys.argv[1]):
                output_line(line)
        elif len(sys.argv) == 1:
            output_line(line)
        else:
            print('Слишком много аргументов')
            sys.exit(1)
