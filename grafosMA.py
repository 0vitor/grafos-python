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
      for _ in range(len(vertices)):
        self.matriz.append([0]*len(self.vertices))

  def criarAresta(self, indexVertice1, indexVertice2):
    self.vertices[indexVertice1]
    self.vertices[indexVertice2]
    self.matriz[indexVertice1][indexVertice2] += 1
    self.matriz[indexVertice2][indexVertice1] += 1

  def removerAresta(self, indexVertice1, indexVertice2):
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
    for i in range(len(self.vertices)):
      contadorDeVertices += self.calcularGrauVertice(i)
    return contadorDeVertices

  def saoVizinhos(self, indexVertice1, indexVertice2):
    endeco = self.matriz[indexVertice1][indexVertice2]
    if(endeco):
      return True
    return False

  def imprimirGrafo(self):
    print("Número Vértices: {}".format(len(self.vertices)))
    print("Número Arestas: {}".format((self.calcularGrauGrafo()) // 2))
    print("\nMatriz Adjacência: ")
    for x in range(len(self.vertices)):
      linha = self.matriz[x]
      for valor in linha:
          print("{}   ".format(valor), end="")
      print("\n")
      
    print("Vértices e seus Graus: ")
    for x in range(len(self.vertices)):
      print("Vértice {}: {}".format(x+1, self.calcularGrauVertice(x)))
    print("--------------------------------")

class GraphDrawerMA:
  def __init__(self, matriz):
    self.matriz = matriz
    self.vertices = []
    self.n = 0
    self.window = tk.Tk()
    self.canvas = tk.Canvas(self.window, width=800, height=600)
    self.canvas.pack()
    self.canvas.bind('<Button-1>', self.adicionarVertices)
    self.window.mainloop()

  def adicionarVertices(self, event):
    x, y = event.x, event.y
    self.vertices.append((x, y))
    self.canvas.create_oval(x-10, y-10, x+10, y+10, fill='white')
    self.canvas.create_text(x, y-20, text=f'Vértice {len(self.vertices)}')
    if len(self.vertices) > len(self.matriz)-1:
        self.desenharArestas()

  def desenharArestas(self):
    for i in range(len(self.matriz)):
      for j in range(len(self.matriz)):
        curvatura = 7
        if self.matriz[i][j] >= 1:
          x1, y1 = self.vertices[i]
          x2, y2 = self.vertices[j]
          if x1 == x2 and y1 == y2:
            loops = self.matriz[i][j]//2
            self.canvas.create_text(x1, y1 - 50, text=str(loops) + " laços", fill="black")
            self.canvas.create_arc(x1-10, y1-30, x2+10, y2, start=270, extent=359, style=tk.ARC)
          else:
            if self.matriz[i][j] > 1:
              for i in range(self.matriz[i][j]-1):
                cx = (x1 + x2) / 2
                cy = (y1 + y2) / 2 - curvatura
                self.canvas.create_line(x1, y1, cx, cy, fill='black')
                curvatura += 7
              self.canvas.create_line(x1, y1, x2, y2, fill='black')
            else:
              self.canvas.create_line(x1, y1, x2, y2, fill='black')
