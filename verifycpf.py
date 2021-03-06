import random

def validaCPF(cpf, a, b):
    somatorio = 0
    for i in range(9):
        somatorio = somatorio + (11 - (i + 1)) * int(cpf[i])
    
    soma = 11 - (somatorio % 11)
    
    if soma > 9:
        v1 = 0
    else:
        v1 = soma

    soma1 = 0
    
    for i in range(9):
        soma1 = soma1 + (12 - (i + 1)) * int(cpf[i])

    soma2 = 11 - ((soma1 + (v1 * 2)) % 11)
    
    if soma2 > 9:
        v2 = 0
    else:
        v2 = soma2

    if v1 == a:
        d1 = True
    else:
        d1 = False

    if v2 == b:
        d2 = True
    else:
        d2 = False

    if d1 == d2 == True:
        return True
    else:
        return False
#acaba aqui validaCPF

def verificador(cpf):
    somatorio = 0
    for i in range(9):
        somatorio = int(somatorio + (11 - (i + 1)) * int(cpf[i]))

    soma = 11 - (somatorio % 11)

    if soma > 9:
        v1 = 0
    else:
        v1 = soma

    soma1 = 0

    for i in range(9):
            soma1 = soma1 + (12 - (i + 1)) * int(cpf[i])
    
    soma2 = 11 - ((soma1 + (v1 * 2)) % 11)

    if soma2 > 9:
        v2 = 0
    else:
        v2 = soma2

    digitos = [v1, v2]
    return digitos


def geraCpf():
    cpf = [0, 6, 9, 5, 1, 4, 5, 6, 1]
    for i in range(9):
        cpf[i] = int(random.randint(0, 9))
    
    digitos = verificador(cpf)
    cpfCompleto = cpf + digitos

    return cpfCompleto




print("o que voce deseja:")
print("1: validar")
print("2: encontrar digito verificador")
print("3: gerar um cpf aleatorio")

selecao = input()

if selecao == "1":

    cpf = input("9 digitos do CPF\n")

    while len(cpf) != 9:
        cpf = input("CPF invalido, digite novamente\n")

    a = int(input("Digito 1: "))
    b = int(input("Digito 2: "))
    

    if validaCPF(cpf, a, b) == True:
        print("o CPF eh valido")
    else:
        print("o CPF eh invalido")

elif selecao == "2":
    cpf = input("9 digitos do CPF\n")

    while len(cpf) != 9:
        cpf = input("CPF invalido, digite novamente\n")

    digitos = verificador(cpf)
    final = "os digitos sao: {digitos}"
    print(digitos)

elif selecao == "3":
    cpfRandom = geraCpf()
    for i in range(11):
        print(cpfRandom[i], end='')
    print()
    print(cpfRandom)
