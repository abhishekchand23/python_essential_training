def f1(f):
    def f2():
        print('this is before the function call')
        f()
        print('this is after the fuction call')
    return f2

@f1
def f3():
    print('this is f3')   

#all three below do the same 

# x = f1(f3)
# x()

# instead of below use the decorator @f1
# f3 = f1(f3)
# f3()

f3()