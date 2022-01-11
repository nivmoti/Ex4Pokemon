import ast
from typing import List
from src.FWA import FWA
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
from src.DiGraph import DiGraph
import copy
import json
# import matplotlib.pyplot as plt
from queue import PriorityQueue
from src.Node import Node
from src.Que import Que

class GraphAlgo(GraphAlgoInterface):
    # constructor:
    def _init_(self, graph=None):
        self.graph = DiGraph()
        self.graph = copy.copy(graph)
        if (graph != None):
            self.fwa = FWA(self.graph)
            self.v = self.graph.get_all_v()

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, data) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
        ans = True
        g = DiGraph()
        for i in range(len(data["Nodes"])):
            key = "pos"
            if key in data["Nodes"][i]:
                l = data["Nodes"][i]["pos"].split(",")
                t = (l[0], l[1], l[2])
            else:
                t = None
            g.add_node(data["Nodes"][i]["id"], t)
        for i in range(len(data["Edges"])):
            g.add_edge(data["Edges"][i]["src"], data["Edges"][i]["dest"], data["Edges"][i]["w"])
        self._init_(g)
        return ans

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
        """
        data = ast.literal_eval(self.graph._str_())
        file = open(file_name, 'w')
        ans = True
        try:
            json.dump(data, file, indent=2)
        except:
            ans = False
        finally:
            file.close()
            return ans

    # helper of diajxstra
    def relax(self, u: Node, y: Node, w: float):
        if (y.GetD() > u.GetD() + w):
            y.setD(u.GetD() + w)
            y.setDadi(u)
    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if not (id1 in self.v) or not (id2 in self.v):
            return (float('inf'), [])
        for id in self.v:
            self.v[id].setD(float('inf'))
            self.v[id].setDadi(None)
        self.v[id1].d = 0
        q=Que(self.graph)
        while q.isEmpty()==False:
            u = q.remove()
            for y in self.graph.outE[u.id].keys():
                self.relax(u, self.v[y], self.graph.outE[u.id][y])
        list = []
        di = self.v[id2].getKey()
        while (di != id1):
            list.append(di)
            if self.v[id2].getDadi() != None:
                di = self.v[di].getDadi().getKey()
            else:
                list = []
                break
        if len(list) != 0:
            list.append(di)
            list.reverse()
        return (self.v[id2].GetD(), list)

    def isDone(self, isVisit):
        ans = True
        for i in range(len(isVisit)):
            ans = ans and isVisit[i]
            if (ans == False):
                return ans
        return ans

    def nearestN(self, i, node_lst, c, isVisited):
        min = float('inf')
        index = -1
        for j in range(len(node_lst)):
            if (i != j):
                if (c[i][j][0] < min and isVisited[j] == False):
                    min = c[i][j][0]
                    index = j
        if index != -1:
            isVisited[index] = True
        return index

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        """
        Finds the shortest path that visits all the nodes in the list
        :param node_lst: A list of nodes id's
        :return: A list of the nodes id's in the path, and the overall distance
        """
        c = []
        for i in range(len(node_lst)):
            c.append([])
            for j in range(len(node_lst)):
                if (i != j):
                    c[i].append(self.shortest_path(node_lst[i], node_lst[j]))
                else:
                    c[i].append(0)
        min = float('inf')
        ans = []
        for i in range(len(node_lst)):
            isVisited = []
            for j in range(len(node_lst)):
                isVisited.append(False)
            isVisited[i] = True
            temp = []
            temp.append(node_lst[i])
            src = i
            w = 0.0
            no = 1
            while (self.isDone(isVisited) == False):
                index = self.nearestN(i, node_lst, c, isVisited)
                if (index == -1):
                    no = 0
                    break
                temp.pop(len(temp) - 1)
                temp.extend(c[src][index][1])
                w = w + c[src][index][0]
                src = index
            if (no == 1):
                if (min > w):
                    min = w
                    ans = temp
        return [ans, min]

    def centerPoint(self) -> (int, float):
        """
        Finds the node that has the shortest distance to it's farthest node.
        :return: The nodes id, min-maximum distance
        """
        return self.fwa.center()

    def findeMinMax(self):
        minx = float('inf')
        minY = float('inf')
        minZ = float('inf')
        maxX = float('-inf')
        maxY = float('-inf')
        maxZ = float('-inf')
        # print(len(self.v))
        for n in self.v:
            if self.v[n].pos != None:
                if (self.v[n].getx() < minx):
                    minx = self.v[n].getx()
                if (self.v[n].gety() < minY):
                    minY = self.v[n].gety()
                if (self.v[n].getz() < minZ):
                    minZ = self.v[n].getz()
                if (self.v[n].getx() > maxX):
                    maxX = self.v[n].getx()
                if (self.v[n].gety() > maxY):
                    maxY = self.v[n].gety()
                if (self.v[n].getz() > maxZ):
                    maxZ = self.v[n].getz()
        ans = []
        ans.append(minx)
        ans.append(maxX)
        ans.append(minY)
        ans.append(maxY)
        ans.append(minZ)
        ans.append(maxZ)
        return ans

        # def plot_graph(self) -> None:
        #     list=self.findeMinMax()
        #     minX=list[0]
        #     maxX=list[1]
        #     minY=list[2]
        #     maxY=list[3]
        #     minZ=list[4]
        #     maxZ=list[5]
        #     i=0.01
        #     k=0
        #     for n in self.graph.v:
        #         if(self.v[n].pos==None):
        #             if(k%2==0):
        #                 if(minX!=float('inf')):
        #                     self.v[n].setx(minX-i)
        #                     minx=minX-i
        #                     self.v[n].sety(minY - i)
        #                     minY = minY - i
        #                     self.v[n].setz(minZ-i)
        #                     minZ=minZ-i
        #                     k=k+1
        #                     i=i+0.01
        #                 else:
        #                     self.v[n].setx(0 - i)
        #                     minx = 0 - i
        #                     self.v[n].sety(0 - i)
        #                     minY = 0 - i
        #                     self.v[n].setz(0 - i)
        #                     minZ = 0 - i
        #                     k = k + 1
        #                     i = i + 0.01
        #             else:
        #                 if(maxX!=float('-inf')):
        #                     self.v[n].setx(maxX+i)
        #                     maxX=maxX+i
        #                     self.v[n].sety(maxY + i)
        #                     maxY = maxY + i
        #                     self.v[n].setz(maxZ+i)
        #                     maxZ=maxZ+i
        #                     k=k+1
        #                 else:
        #                     self.v[n].setx(0 + i)
        #                     maxX = 0 + i
        #                     self.v[n].sety(0 + i)
        #                     maxY = 0 + i
        #                     self.v[n].setz(0 + i)
        #                     maxZ = 0 + i
        #                     k = k + 1
        #         plt.scatter(self.v[n].getx(), self.v[n].gety(), 20,color="green")
        #         plt.text(self.v[n].getx() + 0.00001,self.v[n].gety() +0.00001, self.v[n].getKey(), None, color="red")
        #     for src in self.graph.outE:
        #        for dest in self.graph.outE[src]:
        #            disx=(self.v.get(dest).getx()-self.v.get(src).getx())
        #            disy=(self.v.get(dest).gety()-self.v.get(src).gety())
        #            plt.arrow(self.v.get(src).getx()-disx/100,self.v.get(src).gety()-disy/100,disx-disx*4/100,disy-disy*4/100,width=0.00005)
        #     plt.show()
        #     return None
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """