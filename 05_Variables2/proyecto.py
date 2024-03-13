# Analizador de texto

# El programa solicita un texto al usuario y tres letras y se haran cinco analisis donde se evalua:
# 1) Cuantas veces aparece la letra
# 2) Cuantas palabras hay en el texto
# 3) Primera y última letra del texto
# 4) Palabras en el orden inverso.
# 5) Si la palabra 'Python' aparece en el texto

userText = input('Ingrese un texto: ')
userText = userText.lower()
text2Analize = userText.lower().split()

print('A continuación, ingrese tres letras para analizar el texto:')

userLetters = []
userLetters.append(input('Ingrese la primera letra: ').lower())
userLetters.append(input('Ingrese la segunda letra: ').lower())
userLetters.append(input('Ingrese la tercera letra: ').lower())

# print('\n')

# print(userText)
# print(text2Analize)
# print(f'Sus letras son: {userA}, {userB}, {userC}')

# 1)

countLetters1 = userText.count(userLetters[0])
countLetters2 = userText.count(userLetters[1])
countLetters3 = userText.count(userLetters[2])

print(f'Analizando el texto con las letras que ingresó, se tiene lo siguiente: \n \t - La letra "{userLetters[0]}" se repite {countLetters1}\n \t - La letra "{userLetters[1]}" se repite {countLetters2} \n \t - La letra "{userLetters[2]}" se repite {countLetters3}')

# 2)

print(f'Hay {len(text2Analize)} palabras en su texto.')

# 3)

print(f'La primera letra de su texto es: {userText[0]}\n La última letra de su texto es: {userText[-1]}')

# 4)

text2Analize.reverse()
print(f'Las palabras en el orden inverso quedan como: {text2Analize}')

# 5)

wordPython = 'python' in userText

if(wordPython == True): 
    print(f'La palabra "Python" aparece en su texto: {userText}')
else :
    print(f"La palabra 'Python' no aparece en su texto: {userText}")
