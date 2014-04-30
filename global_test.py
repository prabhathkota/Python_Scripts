"""
Global
global keyword is required to access the golbal variable

"""

myGlobal = 5

def func1():
    global myGlobal
    myGlobal = 42

def func2():
    print myGlobal

func1()
func2()