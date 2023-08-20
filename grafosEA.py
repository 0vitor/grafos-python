import tkinter as tk

class No:
  def __init__(self, vertice, prox=None):
    self.vertice = vertice
    self.prox = prox

class Vertice:
  def __init__(self, valor, index=-1):
    self.valor = valor
    self.index = index
    self.marca = False
    self.profundidadeEntrada = 0
    self.profundidadeSaida = 0

class Aresta:
  def __init__(self, vertice1, vertice2):
    self.vertice1 = vertice1
    self.vertice2 = vertice2

class GrafoEstrutura:
  def __init__(self):
    self.estrutura = []
    self.ordem = 0
    self.arestaArvore = []
    self.arestaRetorno = []
    self.verticesArvore = []
    self.profundadidadeEntrada = 1
    self.profundidadeSaida = 1

  def verificarVertice(self, vertice):
    for verticeEstrutura in self.estrutura:
      if verticeEstrutura.vertice.valor == vertice.valor: return True
    return False

  def gerarSubgrafo(self, vertices, arestas):
    subgrafo = GrafoEstrutura()
    for vertice in vertices:
      if self.verificarVertice(vertice):
        subgrafo.adicionarVertices([vertice])

    for aresta in arestas:
      if self.saoVizinho(aresta.vertice1, aresta.vertice2):
        subgrafo.criarAresta(aresta.vertice1, aresta.vertice2)
    subgrafo.imprimirGrafo()

  def gerarInduzido(self, vertices):
    subgrafo = GrafoEstrutura()
    for vertice in vertices:
      if self.verificarVertice(vertice):
        subgrafo.adicionarVertices([vertice])

    for vertice1 in vertices:
      for vertice2 in vertices:
        condicao = self.saoVizinho(vertice1, vertice2)
        if condicao:
          nVezes = condicao
          while(nVezes > 0):
            subgrafo.__adicionarNo(vertice1, vertice2)
            nVezes -= 1
    subgrafo.imprimirGrafo()

  def subtrairVertices(self, vertices):
    verticeOut = [elemento.vertice for elemento in self.estrutura if elemento.vertice not in vertices]
    #self.imprimirGrafo()
    self.gerarInduzido(verticeOut)

  def gerarArestaInduzido(self, arestas):
    listaVertices = []
    for aresta in arestas:
      if not aresta.vertice1 in listaVertices: listaVertices.append(aresta.vertice1)
      if not aresta.vertice2 in listaVertices: listaVertices.append(aresta.vertice2)
    self.gerarSubgrafo(listaVertices, arestas)

  def subtrairArestas(self, arestas):
    subgrafo = GrafoEstrutura()
    subgrafo.estrutura = self.estrutura
    for aresta in arestas:
      if self.saoVizinho(aresta.vertice1, aresta.vertice2):
        subgrafo.removerAresta(aresta.vertice1, aresta.vertice2)
    subgrafo.imprimirGrafo()

  def saoVizinho(self, v1, v2):
    nRepeticoes = 0
    for verticeNo in self.estrutura:
      if verticeNo.vertice.valor == v1.valor:
        index = verticeNo.vertice.index
        break
        #print('{} [{}]'.format(verticeNo.vertice.valor, verticeNo.vertice.index))
    #self.imprimirEA()
    if self.estrutura[index].prox == None:
      return nRepeticoes

    verticeNo = self.estrutura[index].prox
    while verticeNo != None:
      if verticeNo.vertice.valor == v2.valor:
        nRepeticoes += 1
      verticeNo = verticeNo.prox
    return nRepeticoes

  def retornaNo(self, vertice):
    for verticeNo in self.estrutura:
      if verticeNo.vertice.valor == vertice.valor:
        return verticeNo

  def __atualizaBP(self, verticeInicial):
    verticeInicial.vertice.marca = True

    vizinho = verticeInicial.prox
    self.verticesArvore.append(verticeInicial.vertice)
    while vizinho:
      if not vizinho.vertice.marca:
        self.__atualizaBP(self.estrutura[vizinho.vertice.index])
      vizinho = vizinho.prox

  def buscaProfunidade(self, verticeInicial):
    verticeInicial.vertice.marca = True

    verticeNo = self.estrutura[verticeInicial.vertice.index]
    verticeNo.vertice.profundidadeEntrada = self.profundadidadeEntrada
    self.profundadidadeEntrada += 1

    vizinho = verticeInicial.prox
    print(verticeInicial.vertice.valor)
    while vizinho:
      tupla = (verticeInicial.vertice, vizinho.vertice)
      tuplaReverse = (vizinho.vertice, verticeInicial.vertice)
      if not vizinho.vertice.marca:
        self.arestaArvore.append(tupla)
        self.buscaProfunidade(self.estrutura[vizinho.vertice.index])
        self.profundidadeSaida += 1
      elif not tuplaReverse in self.arestaArvore and not tuplaReverse in self.arestaRetorno:
          self.arestaRetorno.append(tupla)
      vizinho = vizinho.prox

    verticeInicial.vertice.profundidadeSaida = self.profundidadeSaida

  def encontrarCiclo(self):
    self.buscaProfunidade(self.estrutura[0])
    for v in self.estrutura:
      v.vertice.marca = False

    verticeInicial = self.arestaRetorno[0][1]
    verticeFim = self.arestaRetorno[0][0]

    ciclo = self.encontraPasseio(verticeInicial, verticeFim)

    for vertice in ciclo:
      print(vertice.valor)

  def bp(self, verticeInicial):
    verticeNo = self.retornaNo(verticeInicial)
    self.__atualizaBP(verticeNo)

    for vertice in self.verticesArvore:
      print(f'vertice visitado:', vertice)

  def encontraPasseio(self, verticeInicial, verticeFinal):
    verticeNo = self.retornaNo(verticeInicial)
    self.__atualizaBP(verticeNo)

    listaPasseio = [verticeInicial]

    count = 1
    while count < len(self.verticesArvore):
      #print(self.saoVizinho(self.verticesArvore[3], self.verticesArvore[2]))
      if self.verticesArvore[count].valor == verticeFinal.valor and self.saoVizinho(listaPasseio[-1], self.verticesArvore[count]):
        listaPasseio.append(self.verticesArvore[count])
        passeio = Passeio(listaPasseio)
        passeio.imprimirPasseio()
        return listaPasseio
      if self.saoVizinho(listaPasseio[-1], self.verticesArvore[count]):
        listaPasseio.append(self.verticesArvore[count])
        count += 1
      else:
        listaPasseio.pop()

  def encontraCaminho(self, verticeInicial, verticeFinal):
    self.encontraPasseio(verticeInicial, verticeFinal)

  def transformarEmCaminho(self, caminho):
    i = 0
    j = len(caminho.vertices) - 1
    while i < len(caminho.vertices):
      j = len(caminho.vertices)-1
      while j > i:
        print("i: ", i, "j: ", j)
        #print(caminho.vertices[i].valor, caminho.vertices[-j].valor)
        if caminho.vertices[i] == caminho.vertices[j]:

          for _ in range(i , j):
            caminho.vertices.pop(i+1)

          j = len(caminho.vertices)
          i = 0

        j -= 1
      i += 1




    """ for i in range(len(caminho.vertices)):
      for j in range(i+1, len(caminho.vertices)):
        if caminho.vertices[i] == caminho.vertices[-j]:
          repetido = True
          for _ in range(i, j):
            caminho.vertices.pop(i+1)

        if repetido:
          for i in caminho.vertices:
            print(i.valor)
          self.transformarEmCaminho(caminho)
        return
 """

  def adicionarVertices(self, vertices):
    for vertice in vertices:
      vertice.index = self.ordem
      self.estrutura.append(No(vertice))
      self.ordem += 1

  def __adicionarNo(self, vertice, verticeAdicionado):
    for verticeNoo in self.estrutura:
      if verticeNoo.vertice.valor == vertice.valor:
        vertice.index = verticeNoo.vertice.index

    for verticeNoo in self.estrutura:
      if verticeNoo.vertice.valor == verticeAdicionado.valor:
        verticeAdicionado.index = verticeNoo.vertice.index

    VerticeNo = self.estrutura[vertice.index]
    while VerticeNo.prox != None:
      VerticeNo = VerticeNo.prox
    VerticeNo.prox = No(verticeAdicionado)

  def criarAresta(self, v1, v2):
    self.__adicionarNo(v1, v2)
    self.__adicionarNo(v2, v1)

  def __removerNo(self, v1, v2):
    if self.estrutura[v1.index].vertice.valor == v2.valor:
      self.estrutura[v1.index].prox = self.estrutura[v1.index].prox
    else:
      anterior = None
      atual = self.estrutura[v1.index]
      while atual and (atual.vertice.valor != v2.valor):
        anterior = atual
        atual = atual.prox
      if atual:
        anterior.prox = atual.prox
      else:
        anterior.prox = None

  def removerAresta(self, v1, v2):
    self.__removerNo(v1, v2)
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

  def imprimirEA(self):
    print("Estrutura de Adjacência: ")
    for verticeNo in self.estrutura:
      auxElementNo = verticeNo
      print(auxElementNo.vertice.valor)
      while auxElementNo.prox != None:
        print("No {} -> ".format(auxElementNo.vertice.valor), end="")
        auxElementNo = auxElementNo.prox
      if auxElementNo.vertice != -1:
        print("No {}".format(auxElementNo.vertice.valor))

  def imprimirGrafo(self):
    # Número de vertices e arestas
    print("Número Vértices: {}".format(len(self.estrutura)))
    print("Número Arestas: {}\n".format((self.calcularGrauGrafo()) // 2))
    # Listar arestas
    self.imprimirEA()
    # Listar grau de cada vertice
    print("\nVértices e seus Graus: ")
    for verticeNo in self.estrutura:
      print(
        "Vértice {}: {}".format(
          verticeNo.vertice.valor, self.calcularGrauVertice(verticeNo.vertice)
        )
      )
    print("--------------------------------")

class Passeio:
  def __init__(self, vertices):
    self.vertices = vertices

  def imprimirPasseio(self, reverso=False):
    if reverso == True:
      self.vertices.reverse()

    for i in self.vertices[:len(self.vertices)-1]:
      print(i.valor + " -> ", end="")
    print(self.vertices[len(self.vertices)-1].valor)

    self.vertices.reverse()

  def pegarSecao(self, i, j):
    sessao = self.vertices.copy()
    return sessao[i:j]


class GraphDrawerEA:
  def __init__(self, estruturaAdj):
    self.estruturaAdj = estruturaAdj
    self.verticesRepetidos = []
    self.vertices = []
    self.draw = 1
    self.window = tk.Tk()
    self.canvas = tk.Canvas(self.window, width=800, height=600)
    self.canvas.pack()
    self.canvas.bind("<Button-1>", self.adicionarVertices)
    self.window.mainloop()

  def adicionarVertices(self, event):
    if len(self.vertices) < len(self.estruturaAdj):
      x, y = event.x, event.y
      self.vertices.append((x, y))
      self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="white")
      self.canvas.create_text(x, y - 20, text=f"Vertex {len(self.vertices)}")
    if len(self.vertices) > len(self.estruturaAdj) - 1 and self.draw:
      self.draw = 0
      self.desenharArestas()

  def verificarRepetidos(self, verticeIndex):
    if not (verticeIndex in self.verticesRepetidos):
      self.verticesRepetidos.append(verticeIndex)
      return False
    else:
      return True

  def desenharArestas(self):
    self.canvas.delete("edge")
    for i in range(len(self.estruturaAdj)):
      verticeNo = self.estruturaAdj[i].prox
      curvatura = 7
      loops = 0
      while verticeNo != None:
        x1, y1 = self.vertices[i]
        x2, y2 = self.vertices[verticeNo.vertice.index]

        if self.vertices[i] == self.vertices[verticeNo.vertice.index]:
          loops += 1
          x3 = x1
          y3 = y1
        if self.verificarRepetidos(verticeNo.vertice.index):
          cx = (x1 + x2) / 2
          cy = (y1 + y2) / 2 - curvatura
          self.canvas.create_line(x1, y1, cx, cy, fill="black", tags="edge")
          curvatura += 7
        else:
          self.canvas.create_line(x1, y1, x2, y2, fill="black", tags="edge")
        verticeNo = verticeNo.prox
      if(loops):
        self.canvas.create_text(x3, y3 - 50, text=str(loops//2) + " laços", fill="black")
        self.canvas.create_arc(x3-10, y3-30, x3+10, y3, start=270, extent=359, style=tk.ARC)
      self.verticesRepetidos = []

