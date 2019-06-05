"""
# Using contextlib you don't have to explicitly write __enter__, __exit__
# yield instead of return
"""
import contextlib
import sys
import time


@contextlib.contextmanager
def multiple_context_manager(name):
    print('Entering: {}' . format(name))
    try:
        yield name
        print('Exiting: {}'.format(name))
    except:
        print('context_manager_def_test: EXCEPTION EXIT', sys.exc_info())
        print('Exiting {} with exception {} '.format(name, sys.exc_info()))
        raise

print('*'*75)

with multiple_context_manager('outer') as n1, multiple_context_manager('inner') as n2:
    print('Inside multiple_context_manager BODY')

print('*'*75)
time.sleep(1)

# Here we are catching exceptions in try...catch
with multiple_context_manager('outer') as n1, multiple_context_manager('inner') as n2:
    try:
        print('Inside multiple_context_manager BODY')
        raise ValueError('Something is wrong')
    except:
        print('Inside multiple_context_manager BODY EXCEPTION', sys.exc_info())

print('*'*75)
time.sleep(1)

with multiple_context_manager('outer') as n1, multiple_context_manager('inner') as n2:
    print('Inside multiple_context_manager BODY')
    raise ValueError('Something is wrong')


print('*'*75)

