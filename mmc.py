def mdc(a, b):
    i = a % b
    aux = i
    while i != 0:
        a = b
        b = i
        aux = i
        i = a % b

    return b  

a = int(input("Valor de A: "))
b = int(input("Valor de B: "))

mmc = int((a * b) / mdc(a, b))

print("MMC(A, B) = ", mmc)