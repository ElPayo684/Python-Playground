myTxt = 'Esta es una prueba'
# E s t a   e s   u n a     p  r  u  e  b  a 
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
# 0 -17 ...                                -1

result = myTxt[-4]
print(result)

result = myTxt.index(' ') # Busca a lo largo de la cadena desde el primer caracter
print(result)

result = myTxt.rindex(' ') # Empieza a buscar desde el último caracter
print(result)