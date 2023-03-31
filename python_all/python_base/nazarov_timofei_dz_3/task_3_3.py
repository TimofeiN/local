# "Иван", "Мария", "Петр", "Илья"

def thesaurus(*names):
    all_names = {}

    for name in names:
        key = name[0]
        value = []
        if key in all_names:
            all_names[key].append(name)
        else:
            value.append(name)
            letter_names = {key: value}
            all_names.update(letter_names)
    print(all_names)


thesaurus("Иван", "Мария", "Петр", "Илья")
