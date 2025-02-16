# Bitwise Operators, operator on bits, numbers, these are not logical operators

# & AND, | OR, ^ Xor, << Shift Left, >> Shift Right 

x = 0x0a
y = 0x02
z = x & y

print(f'(hex) x is {x:02x},  y is {y:02x}, z is {z:02x} ')
print(f'(bin) x is {x:08b},  y is {y:08b}, z is {z:08b} ')

x = 0x0a
y = 0x05
z = x | y

print(f'(hex) x is {x:02x},  y is {y:02x}, z is {z:02x} ')
print(f'(bin) x is {x:08b},  y is {y:08b}, z is {z:08b} ')

x = 0x0a
y = 0x05
z = x ^ y

print(f'(hex) x is {x:02x},  y is {y:02x}, z is {z:02x} ')
print(f'(bin) x is {x:08b},  y is {y:08b}, z is {z:08b} ')