class No:
  def __init__(self, vertice, prox = None):
    #O atributo vertice, por agora, armazena index 
    self.vertice = vertice
    self.prox = prox

class Vertice:
  def __init__(self, valor, index):
    self.valor = valor
    self.index = index

class Aresta:
  def __init__(self, vertice1, vertice2):
    self.vertice1 = vertice1
    self.vertice2 = vertice2

class GrafoEstrutura:
  def __init__(self):
    self.__tamanho = 0
    self.vertices = []
    self.estrutura = []
  
  def __iniciarEstrutura(self):
    for _ in self.vertices:
        self.estrutura.append(None)

  def adicionarVertices(self, vertices):
    if self.vertices == []:
      self.vertices = vertices
      self.__iniciarEstrutura()
    else:
      for vertice in vertices:
        self.vertices.append(vertice)
        self.estrutura.append(None)
    self.__tamanho = len(self.vertices)

  def __adicionarNo(self, positionNo, indexNo):
    if  self.estrutura[positionNo] == None:
      self.estrutura[positionNo] = No(indexNo)
    else:
      novoNo = No(indexNo)
      novoNo.prox = self.estrutura[positionNo]
      self.estrutura[positionNo] = novoNo

  def criarAresta(self, indexVertice1, indexVertice2):
    #Restrição para o laço
    self.__adicionarNo(indexVertice1, indexVertice2)
    if indexVertice1 != indexVertice2:
      self.__adicionarNo(indexVertice2, indexVertice1)

  def __removerNo(self, positionNo, indexNo):
    #Caso em que nó é nulo
    if self.estrutura[positionNo] == None: return 
    #Verifica primeiro nó
    if self.estrutura[positionNo].vertice == indexNo:
      self.estrutura[positionNo] = self.estrutura[positionNo].prox
    #Demais nós
    else:
      anterior = None
      corrente = self.estrutura[positionNo]
      while corrente and corrente.vertice != indexNo:
        anterior = corrente
        corrente = corrente.prox
      if corrente:
        anterior.prox = corrente.prox
      else:
        anterior.prox = None

  def removerAresta(self, indexVertice1, indexVertice2):
    #Restrição para o laço
    self.__removerNo(indexVertice1, indexVertice2)
    if indexVertice1 != indexVertice2:
      self.__removerNo(indexVertice2, indexVertice1)

  def calcularGrauVertice(self, positionNo):
    elementNo = self.estrutura[positionNo]
    contadorDeVertices = 0
    while elementNo != None:
      contadorDeVertices += 1
      elementNo = elementNo.prox
    return contadorDeVertices
  
  def calcularGrauGrafo(self):
    contadorDeVertices = 0    
    for idx in range(len(self.estrutura)):
      contadorDeVertices += self.calcularGrauVertice(idx)
    return contadorDeVertices
  
  def imprimirEA(self):
    numPosition = 0
    print("Estrutura de Adjacência: ")
    for elementNo in self.estrutura:
      #Exibe nó da posição
      print("No {}: ".format(numPosition), end = "")
      numPosition += 1
      #Exibe nós que são vizinhos
      if elementNo == None:
        print('')
      else:
        auxElementNo = elementNo
        while auxElementNo.prox != None:
          print("No {} -> ".format(auxElementNo.vertice), end = "")
          auxElementNo = auxElementNo.prox
        if auxElementNo.vertice != -1:
          print("No {}".format(auxElementNo.vertice))

  def eVizinho(self, indexVertice1, indexVertice2):
    elementNo = self.estrutura[indexVertice1]
    while elementNo != None:
      if elementNo.vertice == indexVertice2: return True
      elementNo = elementNo.prox
    return False

  def imprimirGrafo(self):
    #Número de vertices e arestas
    print("Número Vertices: {}".format(self.__tamanho))
    print("Número Arestas: {}\n".format((self.calcularGrauGrafo()) // 2))
    #Listar arestas
    self.imprimirEA()
    #Listar grau de cada vertice
    print("\nVertices e seus Graus: ")
    for idx in range(self.__tamanho):
      print("Vertice {}: {}".format(idx+1, self.calcularGrauVertice(idx)))

def exemploGrafo1():
  grafo = GrafoEstrutura()
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
  grafo = GrafoEstrutura()
  v1 = Vertice("vertice1", 0)
  v2 = Vertice("vertice2", 1)
  v3 = Vertice("vertice3", 2)
  v4 = Vertice("vertice4", 3)
  v5 = Vertice("vertice5", 4)
  grafo.adicionarVertices([v1, v2, v3,v4,v5])
  grafo.criarAresta(0,1)
  grafo.criarAresta(0,2)
  grafo.criarAresta(0,3)
  grafo.criarAresta(0,4)
  grafo.criarAresta(1,2)
  grafo.criarAresta(1,3)
  grafo.criarAresta(1,4)
  grafo.criarAresta(2,3)
  grafo.criarAresta(2,4)
  grafo.criarAresta(3,4)

  grafo.imprimirGrafo()

def teste():
  grafo = GrafoEstrutura()
  v0 = Vertice("vertice1", 0)
  v1 = Vertice("vertice2", 1)
  v2 = Vertice("vertice3", 2)
  v3 = Vertice("vertice4", 3)
  v4 = Vertice("vertice5", 4)
  v5 = Vertice("vertice6", 5)
  
  vertices = [v0, v1, v2, v3]
  extraVertices = [v4, v5]

  grafo.adicionarVertices(vertices)
  grafo.criarAresta(0,1)
  grafo.criarAresta(1,2)
  #grafo.criarAresta(1,1)
  grafo.criarAresta(1,3)
  #grafo.imprimirGrafo()
  grafo.adicionarVertices(extraVertices)
  grafo.imprimirEA()
  #print("Situação: {}".format(grafo.eVizinho(1,4)))
  
def main():
  #teste()
  #exemploGrafo1()
  #exemploGrafo2()
main()

