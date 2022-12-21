#Sets: collecciones desordenadas de objetos únicos.

canasta = {'manzana', 'platano', 'pera', 'manzana', 'naranja', 'pera'}
# print(canasta)

numeros = {1,5,6,7,8,1,1,9,8,3}
# print(numeros)

#tipo 1 de sets: Sets mutables
a = set('abacadabra') #Son mutables se pueden añadir nuevos elementos
# print(a)
a.add('g')
# print(a)

#tipo 2 de sets: Sets inmutables (No se pueden añadir nuevos elementos)
b = frozenset('perro')
print(b)

#Intersecciones
# mi_set = {1, 2, 3, 4, 5}.intersection({3, 4, 5, 6})
mi_set = {1, 2, 3, 4, 5} & {3, 4, 5, 6}
# print(mi_set)

#union
# mi_set_union = {1, 2, 3, 4, 5}.union({3, 4, 5, 6})
mi_set_union = {1, 2, 3, 4, 5} | {3, 4, 5, 6}
# print(mi_set_union)

#diferentes
# mi_set_diferentes = {1, 2, 3, 4}.difference({2, 3, 5})
mi_set_diferentes = {1, 2, 3, 4} - {2, 3, 5}
# print(mi_set_diferentes)

#diferencia simetrica
mi_set_diferentes_simetrica = {1, 2, 3, 4}.symmetric_difference({2, 3, 5})
# print(mi_set_diferentes_simetrica)

mi_set = {1, 2, 3, 4, 5}.issuperset({2, 3, 5})
mi_set = {1, 2, 3, 4, 5}.issubset({2, 3, 5})
# print(mi_set)