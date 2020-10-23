# python built in string functions

class bunny:
    def __init__(self, n):
        self._n = n
    
    def __repr__(self):
        return f'repr: the number of bunnies is {self._n} 👫'
    
    def __str__(self):
        return f'str: the number of bunnies is {self._n}'

x = bunny(47)
print(x)
print(repr(x))
print(ascii(x))
print(ord('👫'))
print(chr(128107))

