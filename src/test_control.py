from unittest import TestCase
from src import DiGraph
from src.DiGraph import DiGraph
from src import GraphAlgo
from src.GraphAlgo import GraphAlgo
from src.control2 import control2
from src.Agent import Agent
from src.control2 import  control2
import json
class Testcontrol(TestCase):
    def test_allocate(self):
        graph = DiGraph()
        graph = DiGraph()
        algo = GraphAlgo()
        file = open('A0.json', 'r')
        algo.load_from_json(json.load(file))
        file.close()
        dic={"Pokemons": [{"Pokemon": {"value": 5.0,"type": -1, "pos": "1.0,0.1,0.0"  } },
                      {"Pokemon": {"value": 5.0,"type": -1, "pos": "1.0,0.2,0.0" } },
                      {"Pokemon": {"value": 5.0, "type": -1, "pos": "1.0,0.3,0.0"}},
                      {"Pokemon": {"value": 10.0, "type": -1, "pos": "0.75,0.0,0.0"}},
                      {"Pokemon": {"value": 10.0, "type": -1, "pos": "0.5,0.0,0.0"}},
                      {"Pokemon": {"value": 10.0, "type": -1, "pos": "0.5,0.0,0.0"}}]}
        arr=[]
        a1=Agent({"id":0,"value": 5.0,"src":2,"dest":-1,"speed":1.0,"pos":"35.18753053591606,32.10378225882353,0.0"},algo)
        a2 = Agent({"id": 1, "value": 5.0, "src":2,"dest": -1, "speed": 1.0, "pos": "35.18753053591606,32.10378225882353,0.0"},algo)
        arr.append(a1)
        arr.append(a2)
        co=control2()
        co.algo=algo
        co.listOfAgent=arr
        poke=co.createPockemon(dic)
        co.allocate()
        self.assertEqual(a1.id,0)