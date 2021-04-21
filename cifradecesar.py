import decimal




def cifra(str, chave, modo):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWYZ'
    strUpper = str.upper()
    
    strEncripted = ''
    for letra in strUpper:
        index = alfabeto.find(letra)
        if index != -1:
            if modo == 0:   #decriptar
                strEncripted += alfabeto[index - chave]
            if modo == 1:   #encriptar
                strEncripted += alfabeto[index + chave]
        else:
            strEncripted += letra
    
    return strEncripted

        
def main():
    print("---------------CIFRA DE CESAR---------------")
    string = input("Frase: ")
    modo = input("Modo:\n0 - Decifrar\n1 - Cifrar\n")
    chave = input("Chave: ")
    print("Resultado: {}".format(cifra(string, int(chave), int(modo))))

main()


