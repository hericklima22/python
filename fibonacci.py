fib = [1]
contador = 1
n = 1
limite = 10


while contador <= limite:
    fib[contador + 1] = n * fib[contador]
    contador += 1
    n = fib[contador - 1]
    print(n)