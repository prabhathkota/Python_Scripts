#########################
# Closure in Python
# A nested function references a value in its enclosing scope.
# We should have a nested function (function within a function).
# The nested function should refer to a value defined in the enclosing function.
# The enclosing function must return the nested function.
# Closures are used as callback functions, this helps in data hiding.
# This helps to reduce the use of global variables.
# When we have few functions in our code, closures are helpful.
# But if we have many functions, then we may go for a class
#########################


# Nested Function
# inner_function() can easily be accessed inside the outer_function body but not outside of it’s body.
# Hence, inner_function() is treated as nested Function which uses text as non-local variable.
def outer_function(text):
    text = text

    def inner_function():
        print(text)

    inner_function()


# A closure — unlike a plain function as above — allows the function to access those enclosed captured variables through
# the closure’s copies of their values or references, even when the function is invoked outside their scope.
def closure_outer_function(text):
    text = text

    def closure_inner_function():
        print(text)

    return closure_inner_function


def enclosed_function(x):
    print('In enclosed_function: ' + str(x))

    def nested_function(y):
        print('###')
        print('In nested_function x : ' + str(x))
        print('In nested_function y : ' + str(y))

    return nested_function    # without parentheses() / callback function


if __name__ == '__main__':
    print('------------------------------------------------------')
    outer_function('Hi Nested Function')
    print('------------------------------------------------------')
    func_obj = closure_outer_function('Hi Closure')
    print(func_obj.__closure__)  # str object text - (<cell at 0x108746b28: str object at 0x108791170>,)
    func_obj()
    print('------------------------------------------------------')
    func_obj = enclosed_function(100)
    print('After calling enclosed_function')
    print(func_obj.__closure__)  # int object x - (<cell at 0x108746b58: int object at 0x108566d00>,)
    func_obj(111)
    print('------------------------------------------------------')


"""
------------------------------------------------------
Hi Nested Function
Hi Closure
------------------------------------------------------
In enclosed_function: 100
After calling enclosed_function
###
In nested_function x : 100
In nested_function y : 111
------------------------------------------------------
"""
