from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
from src.DiGraph import DiGraph
from src.Node import Node
class Que:
    def updatmin(self):
        self.min=0
        if self.isEmpty()==False:
            M=self.list[0].d
            for i in range(len(self.list)):
                if M>self.list[i].d:
                    M=self.list[i].d
                    self.min=i
    def __init__(self,graph):
        self.list=[]
        for k in graph.v:
           self.list.append(graph.v[k])
        self.min=0
        self.updatmin()
    def remove(self):
        ans=self.list[self.min]
        self.list.pop(self.min)
        self.updatmin()
        return ans
    def add(self,n):
        self.list.append(n)
        self.updatmin()
    def isEmpty(self):
        return (len(self.list)==0)