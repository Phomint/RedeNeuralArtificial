from random import *

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
    wk1 = random()
    wk2 = random()

    u = []
    print('wK1: {} \nwK2: {} \n'.format(wk1, wk2))
    for j in range(len(matriz)):
        sigma = 0

        for i in range(len(matriz[j])-1):
            if i == 0:
                result = matriz[j][i]*wk1
                print('x1: {}'.format(result))
            if i == 1:
                result = matriz[j][i]*wk2
                print('x2: {}'.format(result))
            sigma=sigma+result
        print('SIGMA: {}'.format(sigma))
        u.append(sigma)
    return u

def vK(uK):
    oK = random()

    print('\noK: {}'.format(oK))
    v = []
    for u in uK:
        result = u - oK
        print('vK: {}'.format(result))
    v.append(result)
    return v

if __name__ == '__main__':

    local = str(input('Digite local do arquivo: '))

    matriz=criarMatriz(local)
    uk=uK(matriz)
    vK(uk)