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

def deltaGeneralizada(matriz, u, w):
    n = 0.1


    for j in range(len(matriz)):
        delta = []
        e = matriz[j][3]-u[j]
        print('Erro {}'.format(e))
        for i in range(len(matriz[j])-1):
            result = e*n*matriz[j][i]
            delta.append(result)
            print('Delta {}'.format(delta))
            w.__setitem__(i, w[i]+delta[i])
        print('\nNovo W {}'.format(w))
    return w

if __name__ == '__main__':

    local = str(input('Digite local do arquivo: '))

    matriz=criarMatriz(local)
    print(matriz)
    uk=uK(matriz,[0.2,0.2,0.2])
    deltaGeneralizada(matriz, uk, [0.2,0.2,0.2])