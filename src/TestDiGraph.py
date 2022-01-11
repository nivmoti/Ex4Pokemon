import unittest
from src import DiGraph
from src.DiGraph import DiGraph
from src.Node import Node


class TestDiGraph(unittest.TestCase):
    def test_size(self):
        graph1 = DiGraph()
        graph2 = DiGraph()
        graph3 = DiGraph()
        ans=graph1.v_size()
        graph2.add_node(0,(1,0,0))
        graph2.add_node(1, (0, 0, 0))
        graph2.add_node(2, (0, 1, 0))
        graph3.add_node(0, (1, 0, 0))
        graph3.add_node(1, (0, 0, 0))
        graph3.add_node(2, (0, 1, 0))
        graph3.remove_node(2)
        #test size
        self.assertEqual(ans, 0)
        self.assertEqual(graph2.v_size(), 3)
        self.assertEqual(graph3.v_size(), 2)

    def test__node(self):
        graph1 = DiGraph()
        graph2 = DiGraph()
        #test of add
        pos="1,0,0"
        dic={
            "id":0,
            "pos":pos
        }
        n=Node(dic)
        graph2.add_node(0, (1, 0, 0))
        graph2.add_node(1, (0, 0, 0))
        self.assertEqual(n.equal(graph2.get_all_v()[0]),True)
        self.assertIsNotNone(graph2.get_all_v()[1])
        self.assertEqual(graph1.get_all_v().get(0), None)
        self.assertEqual(graph2.add_node(0, (0, 0, 0)),False)
        #test of remove:
        graph2.remove_node(1)
        self.assertIsNone(graph2.get_all_v().get(1))
        self.assertEqual(graph2.remove_node(1),False)
    def test_Edge(self):
        graph2 = DiGraph()
        graph2.add_node(0, (1, 0, 0))
        graph2.add_node(1, (0, 0, 0))
        graph2.add_node(2, (0, 1, 0))
        graph2.add_node(3,(342,1241,32))
        #TEST OF ADD
        graph2.add_edge(0,1,0.1)
        self.assertEqual(graph2.outE[0][1],0.1)
        self.assertEqual(graph2.inE[1][0],0.1)
        self.assertEqual(graph2.add_edge(0,1,0.1),False)
        self.assertEqual((graph2.add_edge(6,8,0.1)),False)
        #TEST OF REMOVE:
        graph2.remove_edge(0,1)
        self.assertEqual(len(graph2.outE[0]),0)
        self.assertTrue(not graph2.remove_edge(0,1))
    def test_mc_getAllV(self):
        graph=DiGraph()
        n1=Node({"id":0,"pos":"0,0,1"})
        n2=Node({"id":1,"pos":"0,2,1"})
        n3=Node({"id":2,"pos":"0,2,1"})
        nodes=[]
        nodes.append(n1)
        nodes.append(n2)
        nodes.append(n3)
        graph.add_node(0,(0,0,1))
        graph.add_node(1,(0,2,1))
        graph.add_node(2,(0,2,1))
        #test of getAllV:
        dic= graph.get_all_v()
        i=0
        for k in dic.keys():
            self.assertTrue(nodes[i].equal(dic[k]))
            i=i+1
        #test of mc:
        graph.add_edge(0,1,0.2)
        graph.add_edge(0,2,0.2)
        graph.add_edge(1,2,0.2)
        graph.remove_edge(1,2)
        graph.add_edge(1,2,0.2)
        graph.remove_node(1)
        self.assertEqual(graph.get_mc(),11)
    def test_outE_inE(self):
        graph=DiGraph()
        graph.add_node(0, (0, 0, 1))
        graph.add_node(1, (0, 2, 1))
        graph.add_node(2, (0, 2, 1))
        graph.add_edge(0, 1, 0.2)
        graph.add_edge(0, 2, 0.2)
        graph.add_edge(1, 2, 0.3)
        graph.add_edge(1, 0, 0.4)
        inE=graph.all_in_edges_of_node(1)
        self.assertEqual(inE[0],0.2)
        outE=graph.all_out_edges_of_node(1)
        self.assertEqual(outE[0],0.4)
        self.assertEqual(outE[2],0.3)