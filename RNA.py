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


if __name__ == '__main__':

    local = str(input('Digite local do arquivo: '))

    print(criarMatriz(local))