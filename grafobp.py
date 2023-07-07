from grafosEA import Vertice, GrafoEstrutura
def grafoEABP():
  grafo = GrafoEstrutura()
  a = Vertice("a", 0)
  b = Vertice("b", 1)
  c = Vertice("c", 2)
  d = Vertice("d", 3)
  e = Vertice("e", 4)
  f = Vertice("f", 5)
  g = Vertice("g", 6)
  h = Vertice("h", 7)
  grafo.adicionarVertices([a, b, c, d, e, f, g, h])
  grafo.criarAresta(a, b)
  grafo.criarAresta(a, c)
  grafo.criarAresta(a, e)
  grafo.criarAresta(a, f)

  grafo.criarAresta(b, d)
  grafo.criarAresta(b, e)

  grafo.criarAresta(c, f)
  grafo.criarAresta(c, g)
  grafo.criarAresta(c, h)

  grafo.criarAresta(f, g)
  grafo.criarAresta(f, h)

  grafo.criarAresta(g, h)

  grafo.bp2(grafo.estrutura[0])
  print("arestas da arvore: ", grafo.arestaArvore)
  print("arestas de retorno: ", grafo.arestaRetorno)
  print("\n-----Profundidades-----\n")
  for v in grafo.estrutura:
    print("vertice: " + v.vertice.valor + ", entrada: ", v.vertice.profundidadeEntrada, ", saida: ", v.vertice.profundidadeSaida)

grafoEATest()
