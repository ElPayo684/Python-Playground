name = 'Carina'

# Inmutable
# name[0] = 'K' Esta linea va a tirar error debido a que una cadena de caracteres es inmutable a menos que se le 
#               reasigne un nuevo valor.
name = 'Karina'
print(name)

# Concatenable
n1 = 'Willi'
n2 = 'am'

print( n1 + n2 )

# Multiplicable

print(n1*10)

# Puede poseer mas de una linea de código:

poema = '''Mil pequeños peces blancos
        como si hirviera
        el color del agua'''

print(poema)

# Comprobable

print('agua' in poema) # Valor booleano que comprueba si hay una sub-cadena especificada en la cadena de caracteres
print(len(poema)) # Cuantos caracteres hay en la cadena