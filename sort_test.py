"""
list.sort() vs sorted()
# list.sort vs sorted()
# list.sort() #sortls only lists
# sorted() function accepts any iterable
#list.sort() method of lists sorts the list in place, while sorted() creates a new list. So if you have a large list, part of your performance difference will be due to copying.

"""


arr_sort = [10, 50, 90, 80, 35, 56, 45, 98]
print "Before list.sort : ", arr_sort
arr_sort.sort()
print "After list.sort  : ", arr_sort

print ""

arr_sort = [10, 50, 90, 80, 35, 56, 45, 98]
print "Before sorted() : ", arr_sort
sorted(arr_sort)
print "After sorted()  : ", arr_sort
print ""
print sorted(arr_sort)
print ""



test_str = "Python is new a SCRIPTING Language"
 
print "Before sorted() : ", test_str
result_list = sorted(test_str.split(), key=str.lower)
print "After sorted()  : ", result_list


# import time
# import random
# test_list1=random.sample(xrange(1000),1000)
# test_list2=random.sample(xrange(1000),1000)
# 
# s=time.time()
# for i in range(10000):
#     test_list1.sort()
# print time.time()-s
# 
# s=time.time()
# for i in range(10000):
#     test_list2=sorted(test_list2)
# print time.time()-s

