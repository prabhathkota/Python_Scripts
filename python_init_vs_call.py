######################################
# __init__ vs __call__
# x = Foo(1, 2, 3) # __init__
# x = Foo()
# x(1, 2, 3) # __call__
######################################


class Foo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        print('In Foo __init__ {}, {}, {}'.format(self.a, self.b, self.c))


class Bar:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self):
        print('In Bar __call__ {}, {}, {}' .format(self.a, self.b, self.c))


if __name__ == '__main__':
    print('--------------------------------------------------')
    f = Foo(100, 200, 300)
    print(f.a)
    #f()    #'Foo' object is not callable
    print('--------------------------------------------------')
    b = Bar(10, 20, 30)
    print(b.a)
    b()
    print('--------------------------------------------------')


"""
Output:

--------------------------------------------------
In Foo __init__ 100, 200, 300
100
--------------------------------------------------
10
In Bar __call__ 10, 20, 30
--------------------------------------------------
"""

