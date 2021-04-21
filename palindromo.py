from typing import Tuple


def palindromo(str):
    frase = str.upper()
    frase = frase.replace(' ', '')
    frase = frase.replace('!', '')
    frase = frase.replace(',', '')
    frase = frase.replace('.', '')
    frase = frase.replace('?', '')
    frase = frase.replace('-', '')
    fraseInvertida = frase[::-1]

    if frase == fraseInvertida:
        return True
    else:
        return False

def main():
    print("---------------PALINDROMO---------------")
    string = input("Digite a frase/palavra: ")
    print("Resultado : {}".format(palindromo(string)))

main()