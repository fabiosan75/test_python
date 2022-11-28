
# lanzar un assert
#assert True == False

# Lanzar excepcion
#if True != False:
#  raise Exception('MEnsaje excepcion')

'''
try:
  print(0 / 0)
except ZeroDivisionError as error:
  print(error)

try:
  assert 1 != 1, 'Uno no es igual a uno'
except AssertionError as error:
  print(error)

try:
  age = 18
  if age < 18:
    raise Exception('No puede ser menor de edad')
except Exception as error:
  print(error)
  
'''

try:
  print(0 / 0)
  assert 1 != 1, 'Uno no es igual a uno 2'
  age = 18
  if age < 18:
    raise Exception('No puede ser menor de edad 2')
except ZeroDivisionError as error:
  print(error) 
except AssertionError as error:
  print(error)
except Exception as error:
  print(error)
  
print('OK')