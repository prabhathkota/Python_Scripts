import timeit



'''
#http://bioportal.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/timeit/index.html
Use of timeit:
The timeit module provides a simple interface for determining the execution time of small bits of Python code
'''

t = timeit.Timer("print 'main statement'", "print 'setup'")

print 'TIMEIT:'
print t.timeit(2)

print '\nREPEAT:'
print t.repeat(3, 2)
