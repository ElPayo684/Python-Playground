alphabetTXT = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

fragment = alphabetTXT[2] # C   Indice 2
print(fragment)
fragment = alphabetTXT[2:5] # CDE   Indices desde el 2 hasta el 5 (el 5 no se incluye)
print(fragment)
fragment = alphabetTXT[2:] # CDEFGHIJKLMNOPQRSTUVWXYZ Indices desde el 2 hasta el último
print(fragment)
fragment = alphabetTXT[2:10:2] # CEGI Indices del 2 al 10 saltando 1
print(fragment)
fragment = alphabetTXT[::3] # ADGJMPSVY Indices desde el inicio que sean cero o multiplo de 3
print(fragment)
fragment = alphabetTXT[::-1] # ZYXWVUTSRQPONMLKJIHGFEDCBA Todos los indices en orden inverso
print(fragment)
