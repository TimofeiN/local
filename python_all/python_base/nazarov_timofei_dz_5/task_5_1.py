"""odd_nums: генератор нечетных чискл от 1 до n"""


def odd_nums(n):
    for num in range(1, n+1, 2):
        yield num


odd_to_15 = odd_nums(15)
while odd_to_15:
    print(next(odd_to_15))
