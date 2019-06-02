######################################################
# Decorators Function with Args
######################################################
import functools


def decorator1(f):
    print('inside decorator1')

    @functools.wraps(f)
    def wrap(*args, **kwargs):
        f(*args, **kwargs)
    return wrap


@decorator1
def test_decorator1_func(*args, **kwargs):
    """ test_decorator1_func documentation """
    print('inside test_decorator1_func')
    print(args)
    print(kwargs)


def return_multiply_decorator(f):
    print('inside return_multiply_decorator')

    @functools.wraps(f)
    def multiply_wrap(*args, **kwargs):
        f(*args, **kwargs)

    return multiply_wrap


@return_multiply_decorator
def return_multiply_func(a, b):
    return a * b


def return_multiply_decorator1(f):
    print('inside return_multiply_decorator1')

    @functools.wraps(f)
    def multiply_wrap1(*args, **kwargs):
        return f(*args, **kwargs)
    return multiply_wrap1


@return_multiply_decorator1
def return_multiply_func1(a, b):
    return a * b


def repeat_decorator_with_args(no_of_times):
    print('inside return_multiply_decorator1')

    def decorator_repeat(f):
        @functools.wraps(f)
        def repeat_wrapper(*args, **kwargs):
            for _ in range(no_of_times):
                f(*args, **kwargs)
        return repeat_wrapper
    return decorator_repeat


@repeat_decorator_with_args(4)
def hello():
    print('Hello, Good Morning!')


if __name__ == '__main__':
    print('------------------------------------')
    test_decorator1_func(10, 20, dic={'key': 'val'})
    print('------------------------------------')
    ret = return_multiply_func(100, 200)
    print(ret)   # None - Your decorator ate the return value from the function
    print('------------------------------------')
    ret1 = return_multiply_func1(100, 200)
    print(ret1)   # 20000
    print('------------------------------------')
    hello()
    print('------------------------------------')


"""
Output:

inside decorator1
inside return_multiply_decorator
inside return_multiply_decorator1
inside return_multiply_decorator1
------------------------------------
inside test_decorator1_func
(10, 20)
{'dic': {'key': 'val'}}
------------------------------------
None
------------------------------------
20000
------------------------------------
Hello, Good Morning!
Hello, Good Morning!
Hello, Good Morning!
Hello, Good Morning!
------------------------------------
"""

