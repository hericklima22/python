from asyncio import sleep
import numpy as np

square = 20

colunas = [0] * square
linhas = [colunas] * square
matriz =str(np.matrix(linhas)).replace('[', ' ').replace(']', ' ')


print(matriz)
input = input()
print(matriz.replace('0', input))