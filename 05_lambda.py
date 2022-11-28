enteros = [1, 2, 4, 7]
def cuadrado(x):
    return x ** 2
def cubo(x):
    return x ** 3
funciones = [cuadrado, cubo]
for e in enteros:
    valores = list(map(lambda x : x(e), funciones))
    print(valores)


def high_order_func(x,func_name):
  return func_name(x)

print(high_order_func(10, cubo))

potencia = lambda x: x * x

print(high_order_func(20, potencia))

result = lambda x,func_name: func_name(x)

print(result(30, potencia))

print(result(25, cuadrado))

numeros = [1,2,3,4]
result = list(map(lambda i: i * 2, numeros))

print(result)


numeros = [1,2,3,4]
numeros_2 = [2,4,6]
result = list(map(lambda x,y: x + y, numeros,numeros_2))

print(result)

