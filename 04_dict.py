import random

dict = {}

for i in range(1,5):
  dict[i] = i * 2

print(dict)

dict = { i: i for i in range(1,5) }
print(dict)

countries = ['col','arg','mx','br']

populations = {country: random.randint(100,600) for country in countries}

print(populations)

result = {country: population for (country, population) in populations.items() if population > 300 }
print(result)

text = 'Cadena de Texto'

chars = {c: c.upper() for c in text if c in 'aeiou' }
print(chars)