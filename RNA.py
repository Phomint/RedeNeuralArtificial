__author__ = 'Patrick Amaral'

def criarMatriz(local):
    matriz=[]

    arq = open(local, 'r')

    for texto in arq.readlines():
        linha = []

        posicao = texto.split()
        x1 = float(posicao[0])
        x2 = float(posicao[1])
        x3 = float(posicao[2])
        y = float(posicao[3])

        linha.append(x1)
        linha.append(x2)
        linha.append(x3)
        linha.append(y)

        matriz.append(linha)

    arq.close()

    return matriz

def uK(matriz, w):
    u = []

    for j in range(len(matriz)):
        sigma = 0

        for i in range(len(matriz[j])-1):
            if i == 0:
                result = matriz[j][i]*w[i]
                print('x1: {}'.format(result))
            if i == 1:
                result = matriz[j][i]*w[i]
                print('x2: {}'.format(result))
            if i == 2:
                result = matriz[j][i]*w[i]
                print('x3: {}'.format(result))
            sigma=sigma+result
        print('SIGMA: {}'.format(sigma))
        u.append(sigma)
    return u

def funcaoLimiar(u):
    for i in range(len(u)):
        if u[i] >= 0:
            u.__setitem__(i, 1)
        if u[i] < 0:
            u.__setitem__(i, 0)
    print('\nYl {}'.format(u))
    return u

def deltaGeneralizada(matriz, yl, w):
    n = 0.1


    for j in range(len(matriz)):
        delta = []
        e = matriz[j][3]-yl[j]
        print('\nErro {}'.format(e))

        for i in range(len(matriz[j])-1):
            result = e*n*matriz[j][i]
            delta.append(result)

            w.__setitem__(i, w[i]+delta[i])
        print('Delta {}'.format(delta))
        print('Novo W {}\n'.format(w))
    return w

if __name__ == '__main__':

    local = str(input('Digite local do arquivo: '))

    matriz = criarMatriz(local)
    print(matriz)
    uk = uK(matriz,[0.2,0.2,0.2])
    yLinha = funcaoLimiar(uk)
    deltaGeneralizada(matriz, yLinha, [0.2,0.2,0.2])