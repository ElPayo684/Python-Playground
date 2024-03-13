# Son similares a las listas, pero se diferencian en que los tupples ocupan menos espacio en la memoria
# porque estas no se pueden modificar, ideal para almacenar datos/estructuras inmutables ene el tiempo

myTuple = (1,2,3,4) # Puede o no llevar parentesis
print(type(myTuple))

myTuple = list(myTuple) # Lo convierte a lista
print(type(myTuple))

myTuple = tuple(myTuple) # Lo convierte a tuple
print(type(myTuple))