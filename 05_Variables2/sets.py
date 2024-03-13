# Los sets se pueden declarar de la siguiente manera:

# set(1,2,3,4,5,6), solo se admite un solo argumento, quedando: set( [1,2,3,4,5,6] )
# {1,2,3,4,5,6}

# Los sets descartan elementos repetidos, e igual no se ordenan por indices y no se pueden ingresar listas o diccionarios

my_set = set( [1,2,3,4,5,(1,2,3),1,1,1,2,2,2,3] ) #No se repiten los valores, y el tuple se reconoce como un valor al ser inmutable
print(type(my_set))
print((my_set))
print(len(my_set))
print(2 in my_set) # Comprueba si un valor se encuentra dentro del set

otroSet = { 1,2,3,4,5,6 }
print(type(otroSet))
print((otroSet))

# Ejemplo

set1 = {1,2,3}
set2 = {3,4,5}

set2.add(6)
set1.remove(1)
set1.discard(7) # Funciona igual que remove, pero este no arroja error si el valor no esta en el set

set3 = set1.union(set2)
print(set3)

set3.pop()
print(set3)