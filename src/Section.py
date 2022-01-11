import copy
import math
from email._header_value_parser import Section

from src.GraphAlgo import GraphAlgo
from src.Pokemon import Pokemon
class Section:
    #constructor
    def __init__(self, listOfvertex=[],listOfPokemon=[],sumOfPokemon=0,graph=GraphAlgo()):
        self.listOfVertex = listOfvertex
        self.listOfPokemons=listOfPokemon
        self.sumOfPekemons=sumOfPokemon
        self.isWasTaked=False
        self.graph=graph
    def Vs(self,start):
        s=[]
        d=[]
        for p in self.listOfPokemons:
            s.append(p.Edge[0])
            d.append(p.Edge[1])
        v=copy.copy(self.graph.shortest_path(start,s[0])[1])
        t=self.graph.TSP(s,d)[0]
        for i in range(0,len(t)-1):
            v.append(t[i])
        self.listOfVertex=v




  #Updates maximum and minimum only of the target
    # because he is the only one who can change them (the source will not change them)
