myNumber = 35

print(myNumber)
print(type(myNumber))

myFloat = 12.3

print(myFloat)
print(type(myFloat))

# Cuando el usuario ingresa un numero, este se registra como un str:

age = input('Digite su edad: ')

print('Su edad es de: ' + age)
print(type(age)) # Es por esta razon que para una operacion aritmetica, este se pase a int

age = int(age)
newAge = int(age) + 1

print(newAge)