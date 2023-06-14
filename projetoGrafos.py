class Vertice:
  def __init__(self, valor, index):
    self.index = index
    #self.vizinhos = []

class Aresta:
  def __init__(self, vertice1, vertice2):
    self.vertice1 = vertice1
    self.vertice2 = vertice2

class GrafoMatriz:
  def __init__(self, tamanhoMax):
    self.tamanho = tamanhoMax
    self.linha = []
    self.coluna = []
    self.matriz = self.__iniciarMatriz()

  def __iniciarMatriz(self):
    matriz = []
    for _ in range(self.tamanho):
        matriz.append([0]*self.tamanho)
    return matriz

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


  def calcularGrau(self):
    contadorDeVertices = 0
    for idx in range(self.tamanho):
      contadorDeVertices += self.calcularGrauVertice(idx)
    return contadorDeVertices

  def eVizinho(self, vertice1, vertice2):
    endeco = self.matriz[vertice1.index][vertice2.index]
    if(endeco):
      return True
    return False

  def imprimirGrafo(self):
    #Número de vertices e arestas
    print("Número Vertices: {}".format(self.tamanho))
    print("Número Arestas: {}".format((self.calcularGrau()) // 2))
    #Podem se tornar funções,  listar arestas e grau de cada vertice
    print("Matriz Adjacencia: ")
    for x in range(self.tamanho):
      linha = self.matriz[x]
      for valor in linha:
          print("{}   ".format(valor), end="")
      print("\n")
    #
    for x in range(self.tamanho):
      print("Vertice {}: {}".format(x, self.calcularGrauVertice(x)))

"""     def criarLigacao(v1, v2):
 """
def main():
  i = GrafoMatriz(3)
  i.imprimirGrafo()
  return
main()
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
