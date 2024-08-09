alfabeto_fonetico = {
        'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Fox',
        'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima',
        'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo',
        'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'Xingu',
        'Y': 'Yankee', 'Z': 'Zulu', '0': 'Negativo', '1': 'Primeiro', '2': 'Segundo', '3': 'Terceiro', '4': 'Quarto',
        '5': 'Quinto', '6': 'Sexto', '7': 'Sétimo', '8': 'Oitavo', '9': 'Nono'}

entrada = str(input("Digite algo: ")).upper()
print('Para caracteres duplicados como `EE` utilizamos o prefixo dobrado, ex "ECHO" dobrado ou "11" primeiro dobrado')
for letra in entrada:
    if letra in alfabeto_fonetico.keys():
        print(f'{letra} = {alfabeto_fonetico[letra]}')
    else:
        print(letra)








