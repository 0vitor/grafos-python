from grafos import *

def exemploGrafo1EA():
  grafo = Grafo("EA")
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
  grafo = Grafo("MA")
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
  grafo = Grafo("EA")
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
  grafo = Grafo("MA")
  v1 = Vertice("vertice1", 0)
  v2 = Vertice("vertice2", 1)
  v3 = Vertice("vertice3", 2)
  v4 = Vertice("vertice4", 3)
  v5 = Vertice("vertice5", 4)
  vertices = [v1, v2, v3, v4, v5]
  grafo.adicionarVertices(vertices)

  for n in vertices:
    for x in vertices:
      if grafo.saoVizinhos(n.index, x.index) or n.index == x.index:
        continue
      grafo.criarAresta(n.index,x.index)

  grafo.imprimirGrafo()
  return grafo

def testeEstrutura():
  #Teste utilizando todas as funções geradas pelo exercício
  grafo = Grafo("EA")
  v1 = Vertice("vertice1", 0)
  v2 = Vertice("vertice2", 1)
  v3 = Vertice("vertice3", 2)
  v4 = Vertice("vertice4", 3)
  v5 = Vertice("vertice5", 4)
  grafo.adicionarVertices([ v1, v2, v3, v4, v5 ])
  grafo.criarAresta(v1,v2)
  grafo.criarAresta(v2,v3)
  grafo.criarAresta(v2,v4)
  grafo.criarAresta(v2,v5)
  grafo.criarAresta(v3,v3)
  grafo.criarAresta(v3,v3)
  grafo.criarAresta(v3,v4)
  grafo.criarAresta(v4,v5)
  print("PÓS ADIÇÃO:")
  grafo.imprimirGrafo()

  grafo.removerAresta(v2,v5)
  grafo.removerAresta(v3,v3)
  print("PÓS REMOÇÃO:")
  grafo.imprimirGrafo()
  
  print("SÃO VIZINHOS:")
  print('(v2,v3): {}'.format(grafo.saoVizinhos(v2,v3)))
  print('(v2,v5): {}'.format(grafo.saoVizinhos(v2,v5)))
  print("--------------------------------\n")
  return grafo

def testeMatriz():
  #Teste utilizando todas as funções geradas pelo exercício
  grafo = Grafo("MA")
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
  grafo.criarAresta(2,2)
  grafo.criarAresta(2,2)
  grafo.criarAresta(2,3)
  grafo.criarAresta(3,4)
  print("PÓS ADIÇÃO:")
  grafo.imprimirGrafo()

  grafo.removerAresta(1,4)
  grafo.removerAresta(2,2)
  print("PÓS REMOÇÃO:")
  grafo.imprimirGrafo()
  
  print("SÃO VIZINHOS:")
  print('(1,2): {}'.format(grafo.saoVizinhos(1,2)))
  print('(1,4): {}'.format(grafo.saoVizinhos(1,4)))
  print("--------------------------------\n")
  return grafo
