a = int(input("Valor de A: "))
b = int(input("Valor de B: "))

i = a % b
aux = i
while i != 0:
    a = b
    b = i
    aux = i
    i = a % b

print("MDC(A,B) = ", b)    
