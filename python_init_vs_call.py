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

    def __call__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


if __name__ == '__main__':
    #f = Foo(100, 200, 300)
    #print(f.a)
    f1 = Foo()
    f1(100, 200, 300)
    print(f1.c)

