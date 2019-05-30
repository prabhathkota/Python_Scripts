######################################
# Applying a class decorator creates a new instance
# So the instance must be callable, __call__ method needs to be implemented
######################################


class CallCount:
    def __init__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)


@CallCount
def hello(name):
    print('Hello, {} '. format(name))


if __name__ == '__main__':
    hello('Test1')
    hello('Test2')
    hello('Test3')
    print(hello.count)
    hello('Test4')
    hello('Test5')
    hello('Test6')
    print(hello.count)

