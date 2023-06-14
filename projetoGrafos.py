class Vertice:
  def __init__(self, valor, index):
    self.valor = valor
    self.index = index

class Aresta:
  def __init__(self, vertice1, vertice2):
    self.vertice1 = vertice1
    self.vertice2 = vertice2

class GrafoMatriz:
  def __init__(self, tamanhoMax):
    self.tamanho = tamanhoMax
    self.vertices = []
    self.matriz = self.__iniciarMatriz()

  def __iniciarMatriz(self):
    matriz = []
    for _ in range(self.tamanho):
        matriz.append([0]*self.tamanho)
    return matriz

  def adicionarVertices(self, vertices):
    self.vertices = vertices

  def criarAresta(self, indexVertice1, indexVertice2):
    self.vertices[indexVertice1]
    self.vertices[indexVertice2]
    self.matriz[indexVertice1][indexVertice2] += 1
    self.matriz[indexVertice2][indexVertice1] += 1

  def removerArestas(self, indexVertice1, indexVertice2):
    endeco = self.matriz[indexVertice1][indexVertice2]
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
  v1 = Vertice("vertice1", 0)
  v2 = Vertice("vertice2", 1)
  v3 = Vertice("vertice3", 2)
  v4 = Vertice("vertice4", 3)
  a1 = Aresta(v1, v2)
  a2 = Aresta(v3, v4)
  """ v0 v1
  v0[ 0   0  ]
  vi[ 0   0  ]

  """

  grafo = GrafoMatriz(4)
  grafo.adicionarVertices([v1, v2, v3, v4])
  grafo.criarAresta(0, 1)
  grafo.criarAresta(2, 3)
  grafo.imprimirGrafo()

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
