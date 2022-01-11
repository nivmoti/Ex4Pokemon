
from src.GraphAlgo import GraphAlgo

class Agent:
    def __init__(self,dic={},algo=GraphAlgo()):
        self.id=dic["id"]
        self.value=dic["value"]
        self.src=dic["src"]
        self.dest=dic["dest"]
        self.speed=dic["speed"]
        self.x=dic["pos"].split(",")[0]
        self.y = dic["pos"].split(",")[1]
        self.pos=dic["pos"]
        if self.pos!="":
            st=self.pos.split(",")
            self.point=(float(st[0]),float(st[1]))
        self.time={}
        self.end=algo.centerPoint()
        self.vertex=[]
        self.kilometePeSecond=0.0
        self.numberofvertex=0
        self.canGetVertex=True
        self.index=0
        self.indexj=0
        #self.getVertex=False
    def AddTime(self,time):
        self.time=time

    def update(self, dic):
        if dic["id"]==self.id:
            self.id = dic["id"]
            self.value = dic["value"]
            self.src = dic["src"]
            self.dest = dic["dest"]
            self.speed = dic["speed"]
            self.x = dic["pos"].split(",")[0]
            self.y = dic["pos"].split(",")[1]
            self.pos = dic["pos"]
    def updateGet(self):
        if len(self.vertex)!=0 and self.index!=len(self.vertex):
           self.getvertex= True

    def getnext(self):
        ans=0
        if self.index<len(self.vertex)-1 :
            self.index = self.index + 1
            self.nextN=self.vertex[self.index]
            return self.nextN
        elif  self.index<len(self.vertex):
            ans =self.vertex[self.index]
            self.index=0
            return ans
        else:
            return -2



    def setVertex(self,v):
        self.vertex=v
        self.end=self.vertex[len(self.vertex)-1]
        self.index=0
    def updateIndex(self):
        if self.index<len(self.vertex)-1:
            self.index=self.index+1
        else:
            self.index=0
    def __str__(self):
        ans= "{id:"+str(self.id)+",v:"
        for v in self.vertex:
            ans=ans+str(v)+","
        ans=ans+"}"
        return ans
    def ontheway(self):
        if(len(self.vertex)<=0):
            return False
        else:
            return True
    def Getnextnode(self):
       return '{"agent_id":' + str(self.id) + ', "next_node_id":' + str(self.getnext()) + '}'