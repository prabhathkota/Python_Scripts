"""
# Using contextlib you don't have to explicitly write __enter__, __exit__
# yield instead of return
"""
import contextlib
import sys
import time

@contextlib.contextmanager
def context_manager_def_test():
    print('context_manager_def_test: ENTER')
    try:
        yield 'You are in with-block'
        print('context_manager_def_test: NORMAL EXIT')
    except Exception:
        print('context_manager_def_test: EXCEPTION EXIT', sys.exc_info())
        raise

print('*'*75)

with context_manager_def_test() as cm:
    print('Inside ContextManagerTest')
    print(cm)

print('*'*75)
time.sleep(1)

with context_manager_def_test() as cm:
    print('Inside ContextManagerTest')
    print(cm)
    raise ValueError('something is wrong')

print('*'*75)


"""
***************************************************************************
context_manager_def_test: ENTER
Inside ContextManagerTest
You are in with-block
context_manager_def_test: NORMAL EXIT
***************************************************************************
context_manager_def_test: ENTER
Inside ContextManagerTest
You are in with-block
context_manager_def_test: EXCEPTION EXIT (<class 'ValueError'>, ValueError('something is wrong'), <traceback object at 0x1023ed0c8>)
Traceback (most recent call last):
  File "/Users/prabhathkota/Workspace/prabhath/personal/Python_Scripts/context_managers/contextlib_example.py", line 31, in <module>
    raise ValueError('something is wrong')
ValueError: something is wrong
***************************************************************************
"""

