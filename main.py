import json
from types import SimpleNamespace

import numpy as np
from numpy.dual import norm

import client
from client import Client
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
from src.Pokemon import Pokemon
from src.Node import Node

if __name__ == '__main__':
    clinet= Client()
    # graph_json = clinet.get_graph()
    # file = open("niv", 'w')
    # ans = True
    # try:
    #     json.dump(graph_json, file, indent=2)
    # except:
    #     ans = False
    # finally:
    #     file.close()
    # grap=GraphAlgo()
    # grap.load_from_json("niv")
    # graf=grap.get_graph()
    # Agents=json.load(clinet.get_agents())
    # maxAgent=json.load(clinet.get_info())["GameServer"]["agents"]
    #
    # pokemons=json.load(clinet.get_pokemons())
    # V = graf.get_all_v()
    # #while is begning
    # min=float('inf')
    # currEdge=None
    # pokes=[]
    # pokemons = json.loads(client.get_pokemons(),
    #                       object_hook=lambda d: SimpleNamespace(**d)).Pokemons
    # pokemons = [p.Pokemon for p in pokemons]
    # for p in pokemons:
    #     poke=Pokemon(p.valu,p.type,p.pos)
    #     for a in V:
    #       for b in graf.all_out_edges_of_node(a.getKey()).keys():
    #           if(p.type==1 and a>b) or (p.type==-1 and a<b):
    #             Edge=(a.getKey(),b)
    #             d=distancePointfromLine(V,poke,Edge)
    #             if(abs(d) <min):
    #                 currEdge=Edge
    #     poke.SetEdge(currEdge)
    #     pokes.append(poke)
