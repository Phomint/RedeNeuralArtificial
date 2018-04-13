import random

__author__ = 'Patrick Amaral'

def criarMatriz(local):
    matriz=[]

    arq = open(local, 'r')

    for texto in arq.readlines():
        linha = []

        posicao = texto.split()
        x1 = float(posicao[0])
        x2 = float(posicao[1])
        y = float(posicao[2])

        linha.append(x1)
        linha.append(x2)
        linha.append(y)

        matriz.append(linha)

    arq.close()

    return matriz

def uK(matriz):
    wk1 = random.random()
    wk2 = random.random()

    print('WK1: {} WK2: {}'.format(wk1, wk2))
    for j in range(len(matriz)):
        sigma = 0
        u=[]
        for i in range(len(matriz[j])-1):
            if i == 0:
                result = matriz[j][i]*wk1
                print('X1: {}'.format(result))
            if i == 1:
                result = matriz[j][i]*wk2
                print('X2: {}'.format(result))
            sigma=sigma+result
        print('SIGMA: {}'.format(sigma))
        u.append(sigma)
    return u

if __name__ == '__main__':

    local = str(input('Digite local do arquivo: '))

    print(criarMatriz(local))
    uK(criarMatriz(local))