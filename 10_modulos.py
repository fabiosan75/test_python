import sys
#print(sys.path)

import re
# Expresion regulares

import time
print(time.time())
print(time.localtime())
print(time.asctime(time.localtime()))

import collections
numbers = [1,2,1,4,78,5,4,8,3,4,5,6,7,8,12]
# Numero de conincidencias en una lista
print(collections.Counter(numbers)) 
