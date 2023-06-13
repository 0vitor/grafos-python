class Vertice:
    def __init__(self, valor, index):
        self.index = index
        self.vizinhos = []

class Aresta:
    def __init__(vertice1, vertice2):
        self.vertice1 = vertice1
        self.vertice2 = vertice2

class GrafroMatriz:
    def __init__(self, tamanho)
        self.tamanhoMax = tamanho
        self.linha = [v1,v2,v3]
        self.coluna = []
        self.matriz = []

    def __inicarMatriz(self):
        coluna = []
        for _ in range(tamanho):
                coluna.append(0)

        for _ in range(tamanho):
            matriz.append(coluna)

    def addVertice():

    def criarColuna(self):
        for _ in range(tamanho):
            for _ in range(tamanho):
                coluna.append(vertice)

            matriz.append(coluna)

    def adicionarArestas(aresta):
        matriz[aresta.vertice1.index][aresta.vertice2.index] += 1
        matriz[aresta.vertice2.index][aresta.vertice1.index] += 1

    def removerArestas(aresta):
        endeco = matriz[aresta.vertice1.index][aresta.vertice2.index]
        if(endeco)
            matriz[aresta.vertice1.index][aresta.vertice2.index] -= 1
            matriz[aresta.vertice2.index][aresta.vertice1.index] -= 1

    def calcularGrauVertice(verticeIndex):
        linha = matriz[verticeIndex]
        contadorDeVertices = 0
        for valor in linha:
            contadorDeVertices += valor

        return contadorDeVertices

    def calcularGrau():
        contadorDeVertices = 0
        for _ in range(tamanho):
            calcularGrauVertice()
            contadorDeVertices += valor


        return contadorDeVertices

    def eVizinho(vertice1, vertice2):
        endeco = matriz[vertice1.index][vertice2.index]
        if(endeco):
            return True
        return False

    def imprimirGrafo():

        print(tamanho)
        print()

    def criarLigacao(v1, v2):

def main():

class Client:
    def criarGrafo(tipoDeEstrutura, tamanho):
        if(tipoDeEstrutura == 'EA'):
            instanciarEA(tamanho)
        elif(tipoDeEstrutura == 'MA'):
            instanciarMA(tamanho)
        else:
            raise "tipo errado"

    def criarVertice(self, valor):

    def instanciarEA(tamanho):
        return GrafroMatriz()

    def instanciarMA(tamanho):
        return estruturaMatriz()
