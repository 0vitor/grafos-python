class No:
  def __init__(self, vertice, prox=None):
    # O atributo vertice, por agora, armazena index
    self.vertice = vertice
    self.prox = prox
    self.marca = False
    self.profundidadeEntrada = 0
    self.profundidadeSaida = 0

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
    self.arestaArvore = []
    self.arestaRetorno = []
    self.profundadidadeEntrada = 1
    self.profundidadeSaida = 1

  def bp(self, verticeInicial):
    verticeInicial.vertice.marca = True

    verticeNo = self.estrutura[verticeInicial.vertice.index]
    verticeNo.vertice.profundidadeEntrada = self.profundadidadeEntrada
    self.profundadidadeEntrada += 1

    vizinho = verticeInicial.prox
    #print(verticeInicial.vertice.valor)
    while vizinho:
      tupla = (verticeInicial.vertice.valor, vizinho.vertice.valor)
      tuplaReverse = (vizinho.vertice.valor, verticeInicial.vertice.valor)
      if not vizinho.vertice.marca:
        self.arestaArvore.append(tupla)
        self.bp2(self.estrutura[vizinho.vertice.index])
        self.profundidadeSaida += 1
      elif not tuplaReverse in self.arestaArvore and not tuplaReverse in self.arestaRetorno:
          self.arestaRetorno.append(tupla)
      vizinho = vizinho.prox

    verticeInicial.vertice.profundidadeSaida = self.profundidadeSaida


  def criarGrafoCompleto(self):
    for i in range(len(self.estrutura)):
      for j in range(len(self.estrutura)):
        if(self.estrutura[i] != self.estrutura[j]):
          self.criarArestaUnidirecional(self.estrutura[i].vertice, self.estrutura[j].vertice)

  def criarVertices(self, n):
    for i in range(n):
      vertice = Vertice(f'v{i}', i)
      verticeNo = No(vertice)
      self.estrutura.append(verticeNo)

  def adicionarVertices(self, vertices):
    for vertice in vertices:
      self.estrutura.append(No(vertice))

  def criarArestaUnidirecional(self, vertice, verticeAdicionado):
    VerticeNo = self.estrutura[vertice.index]
    while VerticeNo.prox:
      VerticeNo = VerticeNo.prox
    VerticeNo.prox = No(verticeAdicionado)

  def criarGrafoRegularPar(self, tamanho, grau):
    ia = grau//2
    while ia:
      for i in range(tamanho-1):
        verticeNo1 = self.estrutura[i]
        verticeNo2 = self.estrutura[i+1]
        self.criarAresta(verticeNo1.vertice, verticeNo2.vertice)

      primeiro = self.estrutura[0].vertice
      ultimo = self.estrutura[tamanho-1].vertice
      self.criarAresta(ultimo, primeiro)
      ia -= 1

  def transformarGrafoRegularImpar(self, tamanho):
    for i in range(0, tamanho, 2):
      print(i)
      verticeNo1 =  self.estrutura[i].vertice
      verticeNo2 =  self.estrutura[i+1].vertice
      self.criarAresta(verticeNo1, verticeNo2)

  def criarGrafoKReg(self, tamanho, grau):
    self.criarVertices(tamanho)
    if grau % 2 == 0:
      self.criarGrafoRegularPar(tamanho, grau)
    elif tamanho % 2 == 1:
      print("não vai da não")
    elif tamanho % 2 == 0:
      self.criarGrafoRegularPar(tamanho, grau-1)
      self.transformarGrafoRegularImpar(tamanho)

  def verificarBipartido(self, vertices1, vertices2):
    interccao = vertices1 & vertices2
    if interccao:
      return False

    for v1 in vertices1:
      for v2 in vertices1:
        if self.saoVizinho(v1, v2):
          return False

    for v1 in vertices2:
      for v2 in vertices2:
        if self.saoVizinho(v1, v2):
          return False

    return True

  def criarAresta(self, v1, v2):
    self.criarArestaUnidirecional(v1, v2)
    if v1 != v2:
      self.criarArestaUnidirecional(v2, v1)

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
    contadorDsaoVizinhos = 0
    while vizinho != None:
      contadorDsaoVizinhos += 1
      vizinho = vizinho.prox
    return contadorDsaoVizinhos

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

  def saoVizinho(self, v1, v2):
    verticeNo = self.estrutura[v1.index].prox
    while verticeNo != None:
      if verticeNo.vertice == v2:
        return True
      verticeNo = verticeNo.prox
    return False

  def imprimirGrafo(self):
    print("Número Vertices: {}".format(len(self.estrutura)))
    print("Número Arestas: {}".format((self.calcularGrauGrafo()) // 2))
    print("Grau do grafo: {}\n".format((self.calcularGrauGrafo())))
    self.imprimirEA()
    print("\nVertices e seus Graus: ")
    for verticeNo in self.estrutura:
      index = verticeNo.vertice.index
      print(
        "Vertice {}: {}".format(
          index + 1, self.calcularGrauVertice(verticeNo.vertice)
        )
      )

def criarGrafoBipartido():
  grafo = GrafoEstrutura()
  v1 = Vertice("v1", 0)
  v2 = Vertice("v2", 1)
  v3 = Vertice("v3", 2)
  v4 = Vertice("v4", 3)
  v5 = Vertice("v5", 4)
  v6 = Vertice("v6", 4)

  grafo.adicionarVertices([v1, v2, v3, v4, v5])
  grafo.criarAresta(v1,v3)
  grafo.criarAresta(v1,v4)
  grafo.criarAresta(v1,v5)

  grafo.criarAresta(v2,v3)
  grafo.criarAresta(v2,v4)
  grafo.criarAresta(v2,v5)

  grafo.imprimirGrafo()
  #testar com ligação entre si e remover set
  set1 = set([])
  set2 = set([v1])
  print(grafo.verificarBipartido(set1, set2))

def main():
  #grafo = GrafoEstrutura()
  criarGrafoBipartido()

main()
