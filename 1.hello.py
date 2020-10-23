
# import platform

# print("This is python version {}".format(platform.python_version()))

# for accuracy in calculation when working with floats as computer sacrificies accuracy for precision 
# so import the below module

from decimal import *  
x= Decimal('0.20')
print("x is {}".format(x))
print(type(x))

x= 9
print("x is {}".format(x))
print(type(x))

x= 9.0
print("x is {}".format(x))
print(type(x))

x= 'seven "{0:<2}" "{1:>09}"'.format(5,6) #for linespaces before or after
print("x is {}".format(x))
print(type(x))