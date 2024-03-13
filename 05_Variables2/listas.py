myList = ['a', 'b', 'c']
myListDLC = ['d', 'e', 'f']
mySecondList = ['hello', 20, True]

result = len(myList)
print(type(myList))

result = myList[1]
print(result)
result = myList[1:]
print(result)
print(myList + myListDLC)

# Las listas si se pueden soreescribir:

mySecondList[2] = 5.5
print(mySecondList)
mySecondList.append('True') 
print(mySecondList)
mySecondList.pop() # Borrar el último
print(mySecondList)
mySecondList.pop(0) # Borrar con un índice
print(mySecondList)

result = [ 'P', 'P', 'C', 'D', 'S', 'A', 'L', 'V', 'C' ]
print(result)
result.sort() # Valores ordenados de manera ascendente en una "lista" NoneType, es decir, no almacenable
print(result)
result.reverse() # Valores ordenados de manera descendenteen una "lista" NoneType, es decir, no almacenable
print(result)