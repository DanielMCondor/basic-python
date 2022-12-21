import math

numeros = [1, 4, 9, 16, 25]
raices = [int(math.sqrt(x)) for x in numeros]
# print(raices)

v = [ x if x > 10 else '*' for x in numeros ]
print(v)