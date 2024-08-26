# temp converter
# converts F to C
def convert_f_to_c(temp):
    c = (temp - 32) * 5/9
    return c
    # print(c)
    # print('unreachable code')

def convert_c_to_f(temp):
    f = (temp * 9/5) + 32
    return f


def convert(temp, f_or_c):
    """
    Converts temp to far or cel, f_or_c is a string, if 'f', convert
    to far, if 'c', convert to cel.
    """
    if f_or_c == 'f':
        return convert_c_to_f(temp)
    elif f_or_c == 'c':
        return convert_f_to_c(temp)
    else:
        raise ValueError(f"f_or_c needs to be 'f', or 'c', value was {f_or_c}")


def convert2(temp, func):
    return func(temp)


# x = 0
# while x < 10:
#     import pdb; pdb.set_trace() # breakpoint
#     print(x)
