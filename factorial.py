def fatorial(num, escolha):
    prox = 1

    if escolha == '2':
        if num == 0:
            return 1
        else:
            for i in range(num):
                prox = prox * (i + 1)
        
        return prox
    else:
        if num == 0:
            return 1
        else:
            for i in range(num):
                prox = prox * (i + 1)
                print("{}! = {}".format(i + 1, prox))

    
def main():
    print("Fatorial!")
    print("Ver passo a passo?")
    escolha = input("1 = S\n2 = N\n")
    num = int(input("Digite o numero: "))
    if escolha == '2':
        print("{}! = {}".format(num, fatorial(num, escolha)))
    else:
        fatorial(num, escolha)

main()