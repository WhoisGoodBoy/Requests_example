'''
def hi(msg:str):
    return "$$$\n***\n" + msg + "\n***\n$$$"

print(hi("moyi vitannya vashomu domy"))



def dollars(func):
    def inner(*args, **kwargs):
        header, footer = '$' * 3, '$' * 3
        return f'{header}\n{func(*args, **kwargs)}\n{footer}'
    return inner


def stars(func):
    def inner(*args, **kwargs):
        header, footer = '*' * 3, '*' * 3
        return f'{header}\n{func(*args, **kwargs)}\n{footer}'
    return inner




@stars
@dollars
'''


def add_footer_header(sign, quantity):
    def midleveldeco(func):
        def inner(*args, **kwargs):
            footer = sign * quantity
            header = sign * quantity
            return f'{header}\n{func(*args, **kwargs)}\n{footer}'
        return inner
    return midleveldeco


@add_footer_header('*', 20)
@add_footer_header('$', 20)
def hi(msg:str):
    return msg


print(hi('shatsya, zdorovlya'))
