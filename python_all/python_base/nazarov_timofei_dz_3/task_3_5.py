from random import choice
from task_5_check_result import check_result
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n, un_repeat=0):
    """
    Mixes 3 words from three regular_expression_parse lists, in one 'joke' (list of words in random order).

    :param n: makes n-time jokes
    :param un_repeat: if > 0 makes mix of unrepeatable words in result
    :return: list of jokes
    """
    result = []
    while n != 0:
        joke = []
        if un_repeat:
            word_nouns = check_result(nouns, result)
            word_adv = check_result(adverbs, result)
            word_adj = check_result(adjectives, result)
        else:
            word_nouns = choice(nouns)
            word_adv = choice(adverbs)
            word_adj = choice(adjectives)
        joke.extend([word_nouns, word_adv, word_adj])
        joke = ' '.join(joke)
        result.append(joke)
        n = n - 1
    return result


print(get_jokes(3, un_repeat=1))
