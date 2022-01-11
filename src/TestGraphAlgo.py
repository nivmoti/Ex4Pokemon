import json
import unittest
from src import DiGraph
from src.DiGraph import DiGraph
from src import GraphAlgo
from GraphAlgo import GraphAlgo
class TestGraphAlgo(unittest.TestCase):
    def test_shortPath(self):
        graph = DiGraph()
        algo=GraphAlgo()
        file = open('A0.json', 'r')
        algo.load_from_json(json.load(file))
        file.close()
        ShortPath1=algo.shortest_path(0,1)
        self.assertEqual(ShortPath1[0],1.4004465106761335)
        print(ShortPath1)
        ans=[0,1]
        j=0
        for i in ans:
            self.assertEqual(i,ShortPath1[1][j])
            j=j+1
        ShortPath2=algo.shortest_path(3,0)
        print(ShortPath2)
        self.assertEqual(ShortPath2[0],4.702068088352025,)
        ans=[3, 2, 1, 0]
        j=0
        for i in ans:
            self.assertEqual(i,ShortPath2[1][j])
            j=j+1
    def test_center(self):
        graph = DiGraph()
        algo = GraphAlgo()
        file = open('A0.json', 'r')
        algo.load_from_json(json.load(file))
        file.close()
        center=algo.centerPoint()
        self.assertEqual(center[0],7)
        self.assertEqual(center[1],6.806805834715163)
        # self.assertEqual(center[0],0)
        # self.assertEqual(center[1],4)
    def test_TSP(self):
        graph = DiGraph()
        algo = GraphAlgo()
        file = open('A0.json', 'r')
        algo.load_from_json(json.load(file))
        file.close()
        tsp=algo.TSP([0,1,3])
        print(tsp)
        self.assertEqual(tsp[1],4.3086815935816)
        ans=[0, 1, 2, 3]
        j=0
        for a in ans:
           self.assertEqual(tsp[0][j],a)
           j+=1