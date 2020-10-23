print('Hello, World.'.upper())
print('Hello, World.'.swapcase())

# strings are first class objects in python

class MyString(str):
    def __str__(self):
        return self[::-1]

s = MyString('Hello, World.')
print(s)

# Common string methods
print('Hello World come On.'.capitalize())
print('Abhishek chand is'.title())
print('ABHISHEK IS DONE with'.casefold()) #more aggresive than lower

s1 = 'Hello World'
s2 = s1.upper()
print(id(s1))
print(id(s2))
print(s1+ " " + s2)
x = 43
# formatting
print(f'this is the number {x:3f}')
print(f'this is the number {x:b} in binary')

s = 'This is a long string with a bunch of words in it'
print(s.split())
l = s.split()
s2 = ':'.join(l)
print(s2)

