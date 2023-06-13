class Vertice:
    def __init__(self, valor, index):
        self.index = index
        self.vizinhos = []

class Aresta:
    def __init__(self, vertice1, vertice2):
        self.vertice1 = vertice1
        self.vertice2 = vertice2

class GrafroMatriz:
    def __init__(self, tamanho):
        self.tamanhoMax = tamanho
        self.linha = []
        self.coluna = []
        self.matriz = []

    def __inicarMatriz(self):
        coluna = []
        for _ in range(self.tamanho):
                coluna.append(0)

        for _ in range(self.tamanho):
            self.matriz.append(coluna)

    def criarColuna(self):
        for _ in range(self.tamanho):
            for _ in range(self.tamanho):
                self.coluna.append(self.vertice)

            self.matriz.append(self.coluna)

    def adicionarArestas(self, aresta):
        self.matriz[aresta.vertice1.index][aresta.vertice2.index] += 1
        self.matriz[aresta.vertice2.index][aresta.vertice1.index] += 1

    def removerArestas(self, aresta):
        endeco = self.matriz[aresta.vertice1.index][aresta.vertice2.index]
        if(endeco):
            self.matriz[aresta.vertice1.index][aresta.vertice2.index] -= 1
            self.matriz[aresta.vertice2.index][aresta.vertice1.index] -= 1

    def calcularGrauVertice(self, verticeIndex):
        linha = self.matriz[verticeIndex]
        contadorDeVertices = 0
        for valor in linha:
            contadorDeVertices += valor

        return contadorDeVertices

    """ def calcularGrau(self):
        contadorDeVertices = 0
        for _ in range(self.tamanho):
            self.calcularGrauVertice()
            contadorDeVertices += valor
        return contadorDeVertices """

    def eVizinho(self, vertice1, vertice2):
        endeco = self.matriz[vertice1.index][vertice2.index]
        if(endeco):
            return True
        return False

    """ def imprimirGrafo():
        print(self.tamanho)
 """

"""     def criarLigacao(v1, v2):
 """
def main():
  return

""" class Client:
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
        return estruturaMatriz() """
