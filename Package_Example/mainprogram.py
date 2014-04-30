"""
import moduletest

print("Print Hello Value : " , moduletest.printhello())

print("Age of Queen : ", moduletest.ageofqueen)

print("Multipled Value : ", moduletest.timesfour(100))


cfcpiano = moduletest.Piano("Electric", "100 Cms", 12000, 20)   #Constructor or Creating Object
cfcpiano.printdetails()
"""

from moduletest import ageofqueen
from moduletest import printhello
from moduletest import timesfour
from moduletest import Piano

# now try using them
print("Age of Queen : " , ageofqueen)
print("Print Hello Value : " , printhello())

print("Multipled Value : ", timesfour(100))

cfcpiano = Piano("Electric", "100 Cms", 12000, 20)   #Constructor or Creating Object
cfcpiano.printdetails()