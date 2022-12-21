'''
listas.py [matrices]
script en python que calcula y muestra la suma de dos matrices
cuadradas (misma cantidad de renglones y columnas) generados
aleatoriamente. Utilizar comprensión de listas para generar las
matrices de forma aleatoría.
'''

import random

N = 3
print(f'Programa que calcula la suma de matrices de tamaño {N}x{N}')
m1 = [[random.randint(1, 50) for j in range(N)] for i in range(N)]
m2 = [[random.randint(1, 50) for j in range(N)] for i in range(N)]
# resultado = [[0]*N for i in range(N)]

#TODO: SUMA DE MATRICES DE MANERA LARGA
'''for fila in range(N):
     for columna in range(N):
         resultado[fila][columna] = m1[fila][columna] + m2[fila][columna]

for i in range(N):
    if i == N//2:
        print(f'{m1[i]} + {m2[i]} = {resultado[i]}')
    else:
        print(f'{m1[i]}  {m2[i]}  {resultado[i]}')
'''

#TODO: SUMA DE MATRICES DE MANERA CORTA
resultado = [[m1[i][j]+m2[i][j] for j in range(N)] for i in range(N)]
for i in range(N):
    print(f'{m1[i]} + {m2[i]} = {resultado[i]}') if i == N//2 else print(f'{m1[i]}  {m2[i]}  {resultado[i]}')



# print('Matriz 01: ', m1)
# print('Matriz 02: ', m2)
# print('Resultado: ', resultado)
