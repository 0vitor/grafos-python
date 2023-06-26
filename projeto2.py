class No:
  def __init__(self, vertice, prox=None):
    # O atributo vertice, por agora, armazena index
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
    self.estrutura = []

  def ligarVertices(self):
    for i in range(len(self.estrutura)):
      for j in range(len(self.estrutura)):
        if(self.estrutura[i] != self.estrutura[j]):
          self.__adicionarNo(self.estrutura[i].vertice, self.estrutura[j].vertice)

  def criarGrafoKn(self, n):
    for i in range(n):
      vertice = Vertice(f'v{i}', i)
      verticeNo = No(vertice)
      self.estrutura.append(verticeNo)

  def adicionarVertices(self, vertices):
    for vertice in vertices:
      self.estrutura.append(No(vertice))

  def adicionarNo(self, vertice, verticeAdicionado):
    VerticeNo = self.estrutura[vertice.index]
    while VerticeNo.prox:
      VerticeNo = VerticeNo.prox
    VerticeNo.prox = No(verticeAdicionado)

  def regularPar(self, tamanho, grau):
    while grau:
      for i in range(tamanho-1):
        verticeNo1 =  self.estrutura[i]
        verticeNo2 =  self.estrutura[i+1]
        self.__adicionarNo(verticeNo1.vertice, verticeNo2.vertice)

      primeiro = self.estrutura[0].vertice
      ultimo = self.estrutura[tamanho-1].vertice
      self.__adicionarNo(ultimo, primeiro)
      grau -= 1

  def regularImpar(self, tamanho):
    for i in range(0, tamanho, 2):
      print(i)
      verticeNo1 =  self.estrutura[i].vertice
      verticeNo2 =  self.estrutura[i+1].vertice
      self.criarAresta(verticeNo1, verticeNo2)

  def criarGradoKReg(self, tamanho, grau):
    self.criarGrafoKn(tamanho)
    if grau % 2 == 0:
      self.regularPar(tamanho, grau)
    elif tamanho % 2 == 1:
      print("não vai da não")
    elif tamanho % 2 == 0:
      self.regularPar(tamanho, grau-1)
      self.regularImpar(tamanho)

  def verificarBipartidoCompleto(self, vertices1, vertices2):
    for i in range(len(vertices1) - 1):
      if self.eVizinho(vertices1[i], vertices1[i+1]):
        return False

    for i in range(len(vertices2) - 1):
      if self.eVizinho(vertices2[i], vertices2[i+1]):
        return False

    for v in vertices1:
      for v2 in vertices2:
        if not self.eVizinho(v, v2):
          return False

    return True

  def criarAresta(self, v1, v2):
    self.adicionarNo(v1, v2)
    if v1 != v2:
      self.adicionarNo(v2, v1)

  def __removerNo(self, v1, v2):
    # Caso em que nó é nulo
    # Verifica primeiro nó
    if self.estrutura[v1.index].vertice == v2:
      self.estrutura[v1.index].prox = self.estrutura[v1.index].prox
    # Demais nós
    else:
      anterior = None
      atual = self.estrutura[v1.index]
      while atual and (atual.vertice != v2):
        anterior = atual
        atual = atual.prox
      if atual:
        anterior.prox = atual.prox
      else:
        anterior.prox = None

  def removerAresta(self, v1, v2):
    self.__removerNo(v1, v2)
    if v1 != v2:
      self.__removerNo(v2, v1)

  def calcularGrauVertice(self, vertice):
    vizinho = self.estrutura[vertice.index].prox
    contadorDeVizinhos = 0
    while vizinho != None:
      contadorDeVizinhos += 1
      vizinho = vizinho.prox
    return contadorDeVizinhos

  def calcularGrauGrafo(self):
    graus = 0
    for verticeNo in self.estrutura:
      graus += self.calcularGrauVertice(verticeNo.vertice)
    return graus

  def imprimirEA(self):
    print("Estrutura de Adjacência: ")
    for verticeNo in self.estrutura:
      auxElementNo = verticeNo
      while auxElementNo.prox != None:
        print("No {} -> ".format(auxElementNo.vertice.index), end="")
        auxElementNo = auxElementNo.prox
      if auxElementNo.vertice != -1:
        print("No {}".format(auxElementNo.vertice.index))

  def eVizinho(self, v1, v2):
    verticeNo = self.estrutura[v1.index]
    while verticeNo != None:
      if verticeNo.vertice == v2:
        return True
      verticeNo = verticeNo.prox
    return False

  def imprimirGrafo(self):
    # Número de vertices e arestas
    print("Número Vertices: {}".format(len(self.estrutura)))
    print("Número Arestas: {}".format((self.calcularGrauGrafo()) // 2))
    print("Grau do grafo: {}\n".format((self.calcularGrauGrafo())))
    # Listar arestas
    self.imprimirEA()
    # Listar grau de cada vertice
    print("\nVertices e seus Graus: ")
    for verticeNo in self.estrutura:
      index = verticeNo.vertice.index
      print(
        "Vertice {}: {}".format(
          index + 1, self.calcularGrauVertice(verticeNo.vertice)
        )
      )
def atividade2_1(n):
  n = 5
  grafo = GrafoEstrutura()
  grafo.criarGrafoKn(n)
  grafo.ligarVertices()
  grafo.imprimirEA()

def caso1(verticePar, grauPar):
  # se o numero de vertices for impar e o graus for par então eu ligo um atras do outro
  grafo = GrafoEstrutura()
  grafo.criarGradoKReg(verticePar, grauPar)
  grafo.imprimirEA()

def criarGrafoBipartido():
  grafo = GrafoEstrutura()
  v1 = Vertice("v1", 0)
  v2 = Vertice("v2", 1)
  v3 = Vertice("v3", 2)
  v4 = Vertice("v4", 3)
  v5 = Vertice("v5", 4)

  grafo.adicionarVertices([v1, v2, v3, v4, v5])
  grafo.adicionarNo(v1,v3)
  grafo.adicionarNo(v1,v4)
  grafo.adicionarNo(v1,v5)

  grafo.adicionarNo(v2,v3)
  grafo.adicionarNo(v2,v4)
  grafo.adicionarNo(v2,v5)

  grafo.adicionarNo(v3,v1)
  grafo.adicionarNo(v3,v2)

  grafo.adicionarNo(v4,v1)
  grafo.adicionarNo(v4,v2)

  grafo.adicionarNo(v5,v1)
  grafo.adicionarNo(v5,v2)
  grafo.imprimirGrafo()
  #print(grafo.verificarBipartidoCompleto([v1, v2], [v3, v4, v5]))


def main():
  grafo = GrafoEstrutura()
  criarGrafoBipartido()

main()
# se o numero de vertices for par e os graus forem pares então liga um atras do outro
# se o numeor de vertices for par e os graus forem impares ligue e pule
