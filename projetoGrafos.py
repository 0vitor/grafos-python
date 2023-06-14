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
      self.matriz[indexVertice1][indexVertice2] -= 1
      self.matriz[indexVertice2][indexVertice1] -= 1

  def calcularGrauVertice(self, indexVertice):
    linha = self.matriz[indexVertice]
    contadorDeVertices = 0
    for valor in linha:
      contadorDeVertices += valor
    return contadorDeVertices

  def calcularGrauGrafo(self):
    contadorDeVertices = 0
    for idx in range(self.tamanho):
      contadorDeVertices += self.calcularGrauVertice(idx)
    return contadorDeVertices

  def eVizinho(self, indexVertice1, indexVertice2):
    endeco = self.matriz[indexVertice1][indexVertice2]
    if(endeco):
      return True
    return False

  def imprimirGrafo(self):
    #Número de vertices e arestas
    print("Número Vertices: {}".format(self.tamanho))
    print("Número Arestas: {}".format((self.calcularGrauGrafo()) // 2))
    #Podem se tornar funções,  listar arestas e grau de cada vertice
    print("Matriz Adjacencia: ")
    for x in range(self.tamanho):
      linha = self.matriz[x]
      for valor in linha:
          print("{}   ".format(valor), end="")
      print("\n")
    #

    for x in range(self.tamanho):
      print("Vertice {}: {}".format(x+1, self.calcularGrauVertice(x)))

def exemploGrafo1():
  grafo = GrafoMatriz(5)
  v1 = Vertice("vertice1", 0)
  v2 = Vertice("vertice2", 1)
  v3 = Vertice("vertice3", 2)
  v4 = Vertice("vertice4", 3)
  v5 = Vertice("vertice5", 4)
  grafo.adicionarVertices([v1, v2, v3,v4,v5])
  grafo.criarAresta(0,1)
  grafo.criarAresta(1,2)
  grafo.criarAresta(1,3)
  grafo.criarAresta(1,4)
  grafo.criarAresta(1,4)
  grafo.criarAresta(2,2)
  grafo.criarAresta(2,3)
  grafo.criarAresta(3,4)

  grafo.imprimirGrafo()

def exemploGrafo2():
  grafo = GrafoMatriz(5)
  v1 = Vertice("vertice1", 0)
  v2 = Vertice("vertice2", 1)
  v3 = Vertice("vertice3", 2)
  v4 = Vertice("vertice4", 3)
  v5 = Vertice("vertice5", 4)
  vertices = [v1, v2, v3,v4,v5]
  grafo.adicionarVertices(vertices)

  for n in vertices:
    for x in vertices:
      if grafo.eVizinho(n.index, x.index) or n.index == x.index:
        continue
      grafo.criarAresta(n.index,x.index)

  grafo.imprimirGrafo()

def teste():
  v0 = Vertice("vertice1", 0)
  v1 = Vertice("vertice2", 1)
  v2 = Vertice("vertice3", 2)
  v3 = Vertice("vertice4", 3)

  grafo = GrafoMatriz(4)
  grafo.adicionarVertices([v0, v1, v2, v3])
  grafo.criarAresta(0, 1)
  grafo.criarAresta(2, 3)
  grafo.criarAresta(1, 3)
  #print(grafo.calcularGrauVertice(3))
  #print(grafo.eVizinho(0,1), grafo.eVizinho(2,3), grafo.eVizinho(2,0))
  grafo.removerArestas(0, 1)
  grafo.imprimirGrafo()

def main():
  #teste()
  #exemploGrafo1()
  exemploGrafo2()
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
