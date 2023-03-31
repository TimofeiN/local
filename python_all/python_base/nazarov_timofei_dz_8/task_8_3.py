from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        output = ''
        for arg in args:
            arg_type = f'({arg}: {type(arg)}), '
            output += arg_type
        print(f'{func.__name__} {output[:-2]}')
        return output
    return wrapper


@type_logger
def calc_cubes(*args):
    res = [int(arg)**3 for arg in args]
    return res


a = calc_cubes(5, '3', 2.0)

