import math

x = 1.553
print(round(x))
print(round(x, 1))

print(math.ceil(x)) # Redondear para arriba
print(math.floor(x)) # Redondear para abajo
print(math.trunc(x)) # Muestra la parte entera de un número

numeros = [1,2,3,4,5]
print(int(math.fsum(numeros))) # suma los numeros de un arreglo
print(math.fsum(numeros)) #suma los numeros de un arreglo

print(int(math.fabs(-4))) # obtine el valor absoluto de un numero (cambia de numero negativo a positivo)
print(math.fabs(-8)) # obtine el valor absoluto de un numero (cambia de numero negativo a positivo)

print(math.fmod(17, 6)) # obtiene el modulo de un numero (17/6) es igual a 2 con residuo o modulo (5)
print(math.exp(2)) # (e) elevado al cuadrado

print(math.pi) # el valor de PI

print(math.pow(5, 6)) # elevado a la potencia
print(math.sqrt(16)) # raiz cuadrada

h = math.hypot(1.5, 1.5) # calcula la hipotenusa de un triángulo
print(h)

r = math.radians(45) #radianes
print("Valor en radianes: {0}".format(r))

print(math.sin(67)) # calcular el seno de 67
print(math.sin(math.radians(30)))

print(math.remainder(16, 2)) #para saber si un numero es divisible (0.00) sino no lo es, será diferente de (0.00)
