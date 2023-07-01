from grafosEA import *
from grafosMA import *

class Grafo:
    def __init__(self, tipo):
        if(tipo == "EA"):
            self.esquema = GrafoEstrutura()
        elif(tipo == "MA"):
            self.esquema = GrafoMatriz()
        else:
            print("Tipo inserido não correspondente!\nInsira MA ou EA")
    
    def adicionarVertices(self, vertices):
        self.esquema.adicionarVertices(vertices)
    
    def criarAresta(self, v1, v2):
        self.esquema.criarAresta(v1, v2)
    
    def removerAresta(self, v1, v2):
        self.esquema.removerAresta(v1, v2)
    
    def calcularGrauVertice(self, vertice):
        self.esquema.calcularGrauVertice(vertice)
    
    def calcularGrauGrafo(self):
        self.esquema.calcularGrauGrafo()
    
    def saoVizinhos(self, v1, v2):
        return self.esquema.saoVizinhos(v1, v2)
    
    def imprimirGrafo(self):
        self.esquema.imprimirGrafo()

    def desenharGrafo(self):
        if type(self.esquema) == type(GrafoEstrutura()):
            GraphDrawerEA(self.esquema.estrutura)
        if type(self.esquema) == type(GrafoMatriz()):
            GraphDrawerMA(self.esquema.matriz)
        

