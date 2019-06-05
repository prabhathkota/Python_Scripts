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
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print('Inside __exit__ without exception')
        else:
            print('Inside __exit__ with exception ({} - {} - {})'.format(exc_type, exc_val, exc_tb))
        return


with ContextManagerTest() as cm:
    print('Inside ContextManagerTest')
    print(cm)


"""
Inside __init__
Inside __enter__
Inside ContextManagerTest
<__main__.ContextManagerTest object at 0x10a920160>
Inside __exit__ without exception
"""

