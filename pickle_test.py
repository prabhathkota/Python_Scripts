import pickle
import cPickle


'''
Use of Pickle:
1) saving a program's state data to disk so that it can carry on where it left off when restarted (persistence)
2) sending python data over a TCP connection in a multi-core or distributed system (marshalling)
3) storing python objects in a database
4) converting an arbitrary python object to a string so that it can be used as a dictionary key (e.g. for caching & memoization).

cPickle is much faster than pickle
First, cPickle can be up to 1000 times faster than pickle because the cPickle is implemented in C. 
Second, in the cPickle module the callables Pickler() and Unpickler() are functions, not classes. This means that you cannot use them to derive custom pickling and unpickling subclasses. 
Most applications have no need for this functionality and should benefit from the greatly improved performance of the cPickle module.

'''


# Save a dictionary into a pickle file.

favorite_color = { "lion": "yellow", "kitty": "red" }

print "Before pickle : ",  favorite_color

cPickle.dump( favorite_color, open( "pickle.txt", "wb" ) )

# Load the dictionary back from the pickle file.

 
favorite_color_new = cPickle.load( open( "pickle.txt", "rb" ) )

print "After load from pickle : ",  favorite_color_new
