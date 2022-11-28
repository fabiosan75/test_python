items = [
  {
    'product': 'pantalon',
    'price': 100,
  },
  {
    'product': 'camisa',
    'price': 300    
  },
  {
    'product': 'pantalones 2',
    'price': 200
  }
]

prices = list(map(lambda item: item['price'], items))

print(items)

# inmutabilidad en el map el dict hace referencia a memoria por lo que
# el dict original se modifica agregando los nuevos valores, crear copy

def add_taxes(item):
  new_item = item.copy()
  new_item['taxes'] = new_item['price'] * .19
  return new_item
  
prices_taxes = list(map(add_taxes, items))

print(prices_taxes)
print(items)