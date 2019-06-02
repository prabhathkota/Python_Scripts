######################################################
# Decorators
# use of functools.wraps
# The @functools.wraps decorator uses the function functools.update_wrapper() to update special attributes
# like __name__ and __doc__ that are used in the introspection.
######################################################
import functools


def decorator1(f):
    print('inside decorator1')

    def wrap(*args, **kwargs):
        f(*args, **kwargs)
    return wrap


@decorator1
def test_decorator1_func():
    """ test_decorator1_func documentation """
    print('inside test_decorator1_func')


def decorator2(f):
    print('inside decorator2')

    def wrap(*args, **kwargs):
        f(*args, **kwargs)
    wrap.__name__ = f.__name__
    wrap.__doc__ = f.__doc__
    return wrap


@decorator2
def test_decorator2_func():
    """ test_decorator2_func documentation """
    print('inside test_decorator2_func')


def decorator3(f):
    print('inside decorator3')

    @functools.wraps(f)
    def wrap(*args, **kwargs):
        f(*args, **kwargs)
    return wrap


@decorator3
def test_decorator3_func():
    """ test_decorator3_func documentation """
    print('inside test_decorator3_func')


if __name__ == '__main__':
    print('------------------------------------')
    # print(help(test_decorator1_func))
    print(test_decorator1_func.__name__)     # wrap
    print(test_decorator1_func.__doc__)      # None
    print(test_decorator1_func.__closure__)  # (<cell at 0x1064d0b28: function object at 0x1064ebe18>,)
    print('------------------------------------')
    # Using functools
    # print(help(test_decorator2_func))
    print(test_decorator2_func.__name__)     # test_decorator2_func
    print(test_decorator2_func.__doc__)      # test_decorator2_func
    print(test_decorator2_func.__closure__)  # (<cell at 0x1064d0b28: function object at 0x10654bc80>,)
    print('------------------------------------')
    # Using functools - this will achieve same as test_decorator2_func
    # print(help(test_decorator3_func))
    print(test_decorator3_func.__name__)     # test_decorator3_func
    print(test_decorator3_func.__doc__)      # test_decorator3_func documentation
    print(test_decorator3_func.__closure__)  # (<cell at 0x10344df18: function object at 0x1034e0d08>,)
    print('------------------------------------')
