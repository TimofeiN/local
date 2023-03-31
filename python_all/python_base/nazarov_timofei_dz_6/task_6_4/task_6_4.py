with open('users.csv', 'r', encoding='utf-8') as users:
    hobbys = open('hobby.csv', 'r', encoding='utf-8')
    for line in users:
        line = line.replace('\n', ' ')
        hobby = hobbys.readline().replace('\n', ' ')
        if hobby == ' ':
            hobby = None
        text = f'{line}: {hobby}\n'
        with open('users_hobby.txt', 'a', encoding='utf-8') as f:
            f.write(text)
    hobbys.close()
