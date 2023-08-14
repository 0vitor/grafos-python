from grafosEA import Passeio, Vertice

def main():
  u = Vertice('u')
  y = Vertice('y')
  v = Vertice('v')
  x = Vertice('x')
  w = Vertice('w')
  passeio = Passeio([u,y,v,x,w])
  passeio.imprimirPasseio()
  passeio.imprimirPasseio(reverse=True)
  sessao = passeio.pegarSecao

main()