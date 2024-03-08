# Crear un programa que calcule las comisiones de los usuarios (13%) que les pregunte por su nombre y cuantas ventas han hecho
# el programa respondera con una frase con su nombre y con el monto que les corresponde

print('--------------------------------------------------------------------------------')
print('---------------------- PROGRAMA PARA CALCULAR SU COMISION ----------------------')
print('--------------------------------------------------------------------------------')

print('\tLa comisión actual es de 13%\n\n')

name = input('Ingrese su nombre: ')
ventas = float(input('Ingrese cuanto fue el valor de las ventas que realizó este mes: '))

print(f'Bienvenido {name}, le corresponde un pago de: ${round(ventas*0.13,2)}')