num_dict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate_adv(eng_number):
    if eng_number[0].isupper():
        eng_number = eng_number.lower()
        result = num_dict.get(eng_number)
        if result:
            print(result.capitalize())
        else:
            print(result)
    else:
        print(num_dict.get(eng_number))


num_translate_adv('Nine')
