#########################
# Global Scope Vs Enclosing Scope Vs Local Scope
# LEGB rule
#   Local(L): Defined inside function/class
#   Enclosed(E): Defined inside enclosing functions(Nested function concept)
#   Global(G): Defined at the uppermost level
#   Built-in(B): Reserved names in Python builtin modules
#########################

message = 'global'


def enclosing():
    message = 'enclosing'

    def local():
        message = 'local'

    print('enclosing message: ', message)
    local()
    print('enclosing message: ', message)


def enclosing_nonlocal():
    message = 'enclosing'

    def local():
        nonlocal message    # This refers to the above message in enclosing scope, not in global scope
        message = 'local'

    print('enclosing message: ', message)
    local()
    print('enclosing message: ', message)


def enclosing_global():
    message = 'enclosing'

    def local():
        global message
        message = 'local'  # Here you are updating message in global scope, not in enclosing scope

    print('enclosing message: ', message)
    local()
    print('enclosing message: ', message)


if __name__ == '__main__':
    print('------------------------------------')
    print('global message: ', message)
    enclosing()
    print('global message: ', message)
    print('----------------NONLOCAL------------------')
    print('global message: ', message)
    enclosing_nonlocal()
    print('global message: ', message)
    print('----------------GLOBAL--------------------')
    print('global message: ', message)
    enclosing_global()
    print('global message: ', message)
    print('------------------------------------')


"""
Output:

------------------------------------
global message:  global
enclosing message:  enclosing
enclosing message:  enclosing
global message:  global
----------------NONLOCAL------------------
global message:  global
enclosing message:  enclosing
enclosing message:  local
global message:  global
----------------GLOBAL--------------------
global message:  global
enclosing message:  enclosing
enclosing message:  enclosing
global message:  local
------------------------------------

"""

