from grafosEA import GraphDrawerEA
from grafosMA import GraphDrawerMA
from exemplos import exemploGrafo1MA, exemploGrafo1EA, exemploGrafo2MA, exemploGrafo2EA

def main():
  grafoEx1MA = exemploGrafo1MA()
  grafoEx2MA = exemploGrafo2MA()
  grafoEx1EA = exemploGrafo1EA()
  grafoEx2EA = exemploGrafo2EA()

  #GraphDrawerMA(grafoEx1MA.matriz)
  #GraphDrawerMA(grafoEx2MA.matriz)
  #GraphDrawerEA(grafoEx1EA.estrutura)
  #GraphDrawerEA(grafoEx2EA.estrutura)

main()
