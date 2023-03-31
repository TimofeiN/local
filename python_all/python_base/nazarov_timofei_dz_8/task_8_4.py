from functools import wraps


def val_checker(func):
    def decor_val_check(_func):
        @wraps(_func)
        def wrapper_check(arg):
            res = func(arg)
            if res:
                print(_func(arg))
            else:
                msg = f' wrong value {arg}'
                raise ValueError(msg)
            return res
        return wrapper_check
    return decor_val_check


@val_checker(lambda num: num > 0)
def calc_cubes(num):
    return num**3


a = calc_cubes(-5)
