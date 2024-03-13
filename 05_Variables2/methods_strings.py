phrase = 'Este es un texto de Eddard'

# Upper
result = phrase.upper()
print(result)
# Lower
result = phrase.lower()
print(result)
# Split
result = phrase.split()
print(result)
# Join
a = 'aprender'
b = 'python'
c = 'es'
d = 'genial'

e = ' '.join([a,b,c,d])
print(e)
e = '-'.join([a,b,c,d])
print(e)
# Find
result = phrase.find('de')
print(result)

# La diferencia entre .index() y .find() es que si un valor no se encuentra en con index(), da error, pero con find()
# da la salida: -1

# Replace
result = phrase.replace('Eddard', 'Eduardo')
print(result)

# Ejercicio

phrase = 'Si la implementación es difícil de explicar, puede que sea una malan idea'
print(phrase.replace('difícil', 'fácil').replace('mala', 'buena'))