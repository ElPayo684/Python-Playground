# Un diccionario no tiene indices, por lo que no tienen orden
# Se diferencia de una lista porque esta tiene una clave única por diccionario, conviene usarlos cuando la relacion entre 
# clave y concepto son mas relevantes que un orden específico (para esos casos son mejores las listas)

diccionario = {'clave1': 'valor', 'clave2': 'valor'} # Las claves deben ser distintas, el contenido/valor es indistinto 

print(diccionario)
print(type(diccionario))

result = diccionario['clave1']
print(result)

# Ejemplo:

client = {'name': 'Juan', 
          'lastName': 'Perez',
          'weightKG': 88,
          'heightm': 1.85}

consulta = client['lastName']

print(consulta)

# Ejemplo 2

dic = {'clave1': 55,
       'clave2': [10,20,30],
       'clave3': {'subclave1': 100,
                  'subclave2': 200}}

dic['clave4'] = 'Hola' #Agrega una clave y valor a una lista

print(dic['clave2'][1])
print(dic['clave3']['subclave2'])
print(dic)

dic['clave4'] = 'Adios' #Sobreescribe un valor en una clave del diccionario
print(dic)

print(dic.values())
print(dic.keys())
print(dic.items())

# Ejercicio 1:

dict = {'clave1': ['a','b','c'],
        'clave2': ['d','e','f']}

print(dict['clave2'][1].upper())

