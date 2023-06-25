import tkinter as tk

class Vertice:
  def __init__(self, valor, index):
    self.valor = valor
    self.index = index

class Aresta:
  def __init__(self, vertice1, vertice2):
    self.vertice1 = vertice1
    self.vertice2 = vertice2

class GrafoMatriz:
  def __init__(self):
    self.vertices = []
    self.matriz = []

  def adicionarVertices(self, vertices):
      self.vertices.extend(vertices)
      for _ in range(len(self.vertices) - len(self.matriz)):
        self.matriz.append([0]*len(self.vertices))

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
    for idx in range(len(self.vertices)):
      contadorDeVertices += self.calcularGrauVertice(idx)
    return contadorDeVertices

  def eVizinho(self, indexVertice1, indexVertice2):
    endeco = self.matriz[indexVertice1][indexVertice2]
    if(endeco):
      return True
    return False

  def imprimirGrafo(self):
    #Número de vertices e arestas
    print("Número Vertices: {}".format(len(self.vertices)))
    print("Número Arestas: {}".format((self.calcularGrauGrafo()) // 2))
    #Podem se tornar funções,  listar arestas e grau de cada vertice
    print("Matriz Adjacencia: ")
    for x in range(len(self.vertices)):
      linha = self.matriz[x]
      for valor in linha:
          print("{}   ".format(valor), end="")
      print("\n")
    #

    for x in range(len(self.vertices)):
      print("Vertice {}: {}".format(x+1, self.calcularGrauVertice(x)))

def exemploGrafo1():
  grafo = GrafoMatriz()
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
  GraphDrawer(grafo.matriz)

def exemploGrafo2():
  grafo = GrafoMatriz()
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
  GraphDrawer(grafo.matriz)


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




class GraphDrawer:
  def __init__(self, matriz):
    self.matriz = matriz
    self.vertices = []
    self.n = 0
    self.window = tk.Tk()
    self.canvas = tk.Canvas(self.window, width=800, height=600)
    self.canvas.pack()
    self.canvas.bind('<Button-1>', self.add_vertex)
    self.window.mainloop()

  def add_vertex(self, event):
    x, y = event.x, event.y
    self.vertices.append((x, y))
    self.canvas.create_oval(x-10, y-10, x+10, y+10, fill='white')
    self.canvas.create_text(x, y-20, text=f'Vertex {len(self.vertices)}')
    if len(self.vertices) > len(self.matriz)-1:
        self.draw_edges()

  def draw_edges(self):
    self.canvas.delete('edge')
    for i in range(len(self.matriz)):
      for j in range(len(self.matriz)):
        curvatura = 7
        if self.matriz[i][j] >= 1:
          x1, y1 = self.vertices[i]
          x2, y2 = self.vertices[j]
          if x1 == x2 and y1 == y2:
            self.canvas.create_oval(x1-20, y1-30, x1+20, y1, outline='black', tags='edge')
          else:
            if self.matriz[i][j] > 1:
              for i in range(self.matriz[i][j]-1):
                cx = (x1 + x2) / 2
                cy = (y1 + y2) / 2 - curvatura
                self.canvas.create_line(x1, y1, cx, cy, fill='black', tags='edge')
                curvatura += 7
              self.canvas.create_line(x1, y1, x2, y2, fill='black', tags='edge')
            else:
              self.canvas.create_line(x1, y1, x2, y2, fill='black', tags='edge')


def main():
  #teste()
  exemploGrafo1()
  #exemploGrafo2()

main()

