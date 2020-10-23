


def main():
    kitten('meow', 'grr', 'purr')
    x= (1,2,3,4,5)
    kitten(x)
    kitten(*x)
    kitten1(Buffy='meow', Zilla="grrr", Brutus="bhau bhau")
    c = dict(Buffy='meow...', Zilla="grrr", Brutus="bhau to to")
    kitten1(**c)

# Variable argument list 
def kitten(*args):
    if len(args):
        for s in args:
            print(s)
    else: print('Meow.')

# keyword arguments
def kitten1(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('Kitten {} says {} '.format(k, kwargs[k]))
    else: print('Meow.')

if __name__== '__main__': main()