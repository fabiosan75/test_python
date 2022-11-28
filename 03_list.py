number = []
for element in range(1,10):
  number.append(element)
  
print(number)

numbers = [element for element in range(1,10)]
print(numbers)

number = []
for element in range(1,10):
  number.append(element * 2)
  
print(number)

numbers = [element * 2 for element in range(1,10)]
print(numbers)

numbers = []
for i in range(1,10):
  if i % 2 == 0:
    numbers.append(element * 2)

print(numbers)

numbers = [ i * 2 for i in range(1,14) if i % 2 == 0 ]
print(numbers)
names = ['pablo','pedro','jose','carlos']
ages = [10,12,20,30]

print(list(zip(names,ages)))

dict_names = {name: age for (name, age) in zip(names,ages)}

print(dict_names)


