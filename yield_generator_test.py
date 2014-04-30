"""
#http://www.jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/

generator/yield
A generator function is defined like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return. 
If the body of a def contains yield, the function automatically becomes a generator function (even if it also contains a return statement). 
generator functions create generator iterators. That's the last time you'll see the term generator iterator, though, since they're almost always referred to as "generators". 
Just remember that a generator is a special type of iterator

yield is just return (plus a little magic) for generator functions

Ref:
http://stackoverflow.com/questions/231767/the-python-yield-keyword-explained

#List comprehesion
>>> mylist = [x*x for x in range(3)] 
>>> for i in mylist:  #Iterable
...    print i
 
These iterables are handy because you can read them as much as you wish, 
but you store all the values in memory and it's not always what you want when you have a lot of values.
----------

#Generators
Generators are iterators, but you can only iterate over them once. 
It's because they do not store all the values in memory, they generate the values on the fly:

>>> mygenerator = (x*x for x in range(3))
>>> for i in mygenerator:
...    print(i)

It is just the same except you used () instead of []. 
BUT, you can not perform for i in mygenerator a second time since generators can only be used once: 
they calculate 0, then forget about it and calculate 1, and end calculating 4, one by one.

--------
Yield is a keyword that is used like return, except the function will return a generator.

>>> def createGenerator():
...    mylist = range(3)
...    for i in mylist:
...        yield i*i
...
>>> mygenerator = createGenerator() # create a generator
>>> print(mygenerator) # mygenerator is an object!
<generator object createGenerator at 0xb7555c34>
>>> for i in mygenerator:
...     print(i)
0
1
4

To master yield, you must understand that when you call the function, 
the code you have written in the function body does not run. 
The function only returns the generator object, this is a bit tricky :-)

Then, your code will be run each time the for uses the generator.

Now the hard part:

The first time the for calls the generator object created from your function, 
it will run the code in your function from the beginning until it hits yield, 
then it'll return the first value of the loop. 
Then, each other call will run the loop you have written in the function one more time, and return the next value, until there is no value to return.

The generator is considered empty once the function runs but does not hit yield anymore. 
It can be because the loop had come to an end, or because you do not satisfy a "if/else" anymore.



"""

def simple_generator_function():
    yield 100
    yield 200
    yield 300
    

our_generator = simple_generator_function()
print next(our_generator)
print next(our_generator)
print next(our_generator)

print ""

for value in simple_generator_function():
    print(value)