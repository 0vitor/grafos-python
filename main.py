from grafosEA import Passeio, Vertice, GrafoEstrutura

def main():
  grafo = GrafoEstrutura()
  a = Vertice('a')
  b = Vertice('b')
  c = Vertice('c')
  d = Vertice('d')
  e = Vertice('e')
  f = Vertice('f')
  g = Vertice('g')
  h = Vertice('h')

  grafo.adicionarVertices([a,b,c,d,e,f,g,h])
  grafo.criarAresta(a, b)
  grafo.criarAresta(a, c)
  grafo.criarAresta(a, e)
  grafo.criarAresta(a, f)
  grafo.criarAresta(b, d)
  grafo.criarAresta(b, e)
  grafo.criarAresta(c, f)
  grafo.criarAresta(c, g)
  grafo.criarAresta(c, h)
  grafo.criarAresta(f ,g)
  grafo.criarAresta(f, h)
  grafo.criarAresta(g, h)

  grafo.criarAresta(d, e)
  #grafo.encontraCaminho(a, e)
  #grafo.encontraCiclo()
  grafo.buscaProfunidade(grafo.estrutura[0])
  print("aresta de arvore: ")
  for i in grafo.arestaArvore:
    print(i[0].valor, i[1].valor)
  #print("aresta de retorno: ", grafo.arestaRetorno)
 #      0   1   2          4
  #passeio = Passeio([a, c, d, b, e, a, b, c, b, b,c,d, f])
  #passeio = Passeio([a, b, c, b, f])

  #grafo.transformarEmCaminho(passeio)
  #for v in passeio.vertices:
  #  print(v.valor)
main()
