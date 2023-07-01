import tkinter as tk

class No:
  def __init__(self, vertice, prox=None):
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

  def adicionarVertices(self, vertices):
    for vertice in vertices:
      self.estrutura.append(No(vertice))

  def __adicionarNo(self, vertice, verticeAdicionado):
    VerticeNo = self.estrutura[vertice.index]
    while VerticeNo.prox:
      VerticeNo = VerticeNo.prox
    VerticeNo.prox = No(verticeAdicionado)

  def criarAresta(self, v1, v2):
    self.__adicionarNo(v1, v2)
    self.__adicionarNo(v2, v1)

  def __removerNo(self, v1, v2):
    if self.estrutura[v1.index].vertice == v2:
      self.estrutura[v1.index].prox = self.estrutura[v1.index].prox
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

  def saoVizinhos(self, v1, v2):
    verticeNo = self.estrutura[v1.index].prox
    while verticeNo != None:
      if verticeNo.vertice == v2:
        return True
      verticeNo = verticeNo.prox
    return False

  def imprimirGrafo(self):
    # Número de vertices e arestas
    print("Número Vértices: {}".format(len(self.estrutura)))
    print("Número Arestas: {}\n".format((self.calcularGrauGrafo()) // 2))
    # Listar arestas
    self.imprimirEA()
    # Listar grau de cada vertice
    print("\nVértices e seus Graus: ")
    for verticeNo in self.estrutura:
      index = verticeNo.vertice.index
      print(
        "Vértice {}: {}".format(
          index + 1, self.calcularGrauVertice(verticeNo.vertice)
        )
      )
    print("--------------------------------")

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
