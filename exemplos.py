from grafosEA import Vertice, GrafoEstrutura
from grafosMA import Vertice, GrafoMatriz

def exemploGrafo1EA():
  grafo = GrafoEstrutura()
  v0 = Vertice("vertice1", 0)
  v1 = Vertice("vertice2", 1)
  v2 = Vertice("vertice3", 2)
  v3 = Vertice("vertice4", 3)
  v4 = Vertice("vertice5", 4)
  grafo.adicionarVertices([v0, v1, v2, v3, v4])
  grafo.criarAresta(v0, v1)
  grafo.criarAresta(v1, v2)
  grafo.criarAresta(v1, v3)
  grafo.criarAresta(v1, v4)
  grafo.criarAresta(v1, v4)
  grafo.criarAresta(v2, v2)
  grafo.criarAresta(v2, v3)
  grafo.criarAresta(v3, v4)
  grafo.imprimirGrafo()
  return grafo

def exemploGrafo1MA():
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
  return grafo

def exemploGrafo2EA():
  grafo = GrafoEstrutura()
  v0 = Vertice("vertice1", 0)
  v1 = Vertice("vertice2", 1)
  v2 = Vertice("vertice3", 2)
  v3 = Vertice("vertice4", 3)
  v4 = Vertice("vertice5", 4)
  grafo.adicionarVertices([v0, v1, v2, v3, v4])
  grafo.criarAresta(v0, v1)
  grafo.criarAresta(v0, v2)
  grafo.criarAresta(v0, v3)
  grafo.criarAresta(v0, v4)
  grafo.criarAresta(v1, v2)
  grafo.criarAresta(v1, v3)
  grafo.criarAresta(v1, v4)
  grafo.criarAresta(v2, v3)
  grafo.criarAresta(v2, v4)
  grafo.criarAresta(v3, v4)
  grafo.imprimirGrafo()
  return grafo

def exemploGrafo2MA():
  grafo = GrafoMatriz()
  v1 = Vertice("vertice1", 0)
  v2 = Vertice("vertice2", 1)
  v3 = Vertice("vertice3", 2)
  v4 = Vertice("vertice4", 3)
  v5 = Vertice("vertice5", 4)
  vertices = [v1, v2, v3, v4, v5]
  grafo.adicionarVertices(vertices)

  for n in vertices:
    for x in vertices:
      if grafo.saoVizinho(n.index, x.index) or n.index == x.index:
        continue
      grafo.criarAresta(n.index,x.index)

  grafo.imprimirGrafo()
  return grafo

def teste():
  grafo = GrafoMatriz()
  v1 = Vertice("vertice1", 0)
  v2 = Vertice("vertice2", 1)
  v3 = Vertice("vertice3", 2)
  v4 = Vertice("vertice4", 3)
  v5 = Vertice("vertice5", 4)
  grafo.adicionarVertices([ v1, v2, v3, v4, v5 ])
  grafo.criarAresta(0,1)
  grafo.criarAresta(1,2)
  grafo.criarAresta(1,3)
  grafo.criarAresta(1,4)
  grafo.criarAresta(1,4)
  grafo.criarAresta(2,2)
  grafo.criarAresta(2,2)
  grafo.criarAresta(2,3)
  grafo.criarAresta(3,4)
  grafo.removerArestas(1,4)
  grafo.removerArestas(2,2)
  grafo.imprimirGrafo()
