tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А',  '10Б', '9А']

gen = ((tutors[i], klasses[i]) if i+1 <= len(klasses) else (tutors[i], None) for i in range(len(tutors)))

print(type(gen))
while gen:
    print(next(gen))
