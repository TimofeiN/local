from random import choice


def check_result(lst, res):
    """
    Cheking for words allready included in result for function get_jokes

    :param lst: list of incoming words for get_jokes function
    :param res: result of function get_jokes, list what is needed to check
    :return: returns word, what is not in result list
    """
    result_str = ' '.join(res)
    word = choice(lst)
    while result_str.find(word) != -1:
        word = choice(lst)
    return word
