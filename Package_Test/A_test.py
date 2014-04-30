"""
import moduletest

print("Print Hello Value : " , moduletest.printhello())

print("Age of Queen : ", moduletest.ageofqueen)

print("Multipled Value : ", moduletest.timesfour(100))


cfcpiano = moduletest.Piano("Electric", "100 Cms", 12000, 20)   #Constructor or Creating Object
cfcpiano.printdetails()
"""

"""
#from A import ageofqueen
#from A import printhello
#from A import timesfour
#from A import Piano

# now try using them
print("Age of Queen : " , ageofqueen)
print("Print Hello Value : " , printhello())

print("Multipled Value : ", timesfour(100))

cfcpiano = Piano("Electric", "100 Cms", 12000, 20)   #Constructor or Creating Object
cfcpiano.printdetails()

"""

#from A import *

from Package_Test import A #Testing __init__.py


print("Age of Queen : " , A.ageofqueen)
print("Print Hello Value : " , A.printhello())

print("Multipledn Value : ", A.timesfour(100))

cfcpiano = A.Piano("Electric", "100 Cms", 12000, 20)   #Constructor or Creating Object
cfcpiano.printdetails()
