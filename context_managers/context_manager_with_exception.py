###################
# __enter__
# __enter__ is called before executing with-statement body
# __exit__
# __exit__ called after with-statement body
# File opening is context managers
###################


class ContextManagerTest:
    def __init__(self):
        print('Inside __init__')

    def __enter__(self):
        print('Inside __enter__')
        return 'returning ... Inside with block'
        # return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print('Inside __exit__ without exception')
        else:
            print('Inside __exit__ with exception ({} - {} - {})' .format(exc_type, exc_val, exc_tb))


with ContextManagerTest() as cm:
    print('Inside ContextManagerTest')
    print(cm)
    raise ValueError('something is wrong')


"""
Traceback (most recent call last):
Inside __enter__
  File "...../Python_Scripts/context_managers/context_manager_with_exception.py", line 30, in <module>
Inside ContextManagerTest
    raise ValueError('something is wrong')
returning ... Inside with block
ValueError: something is wrong
Inside __exit__ with exception (<class 'ValueError'> - something is wrong - <traceback object at 0x1034ba608>)

"""

