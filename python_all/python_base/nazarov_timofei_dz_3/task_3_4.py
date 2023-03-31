
def thesaurus_adv(*names):
    all_names = {}
    for name in names:
        letter_s = name.split()[-1][0]
        letter_n = name[0]
        names_lst = [name]
        by_name = {letter_n: names_lst}
        if letter_s in all_names:
            if letter_n in all_names[letter_s]:
                all_names[letter_s][letter_n].append(name)
            else:
                all_names[letter_s].update(by_name)
        else:
            all_names.update({letter_s: by_name})
    return all_names


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
