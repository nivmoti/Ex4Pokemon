class Pokemon:
    def __init__(self , valu=0, type=0, pos=""):
        self.valu=valu
        self.type=type
        self.pos=pos
        if pos!="":
            st=pos.split(",")
            self.point=(float(st[0]),float(st[1]))
        self.Edge=None
        self.state=0
        self.isAdd=False
    def equal(self,pokemon):
        ans=  self.valu==pokemon.valu and self.type==pokemon.type and self.state==pokemon.state and self.isAdd==pokemon.isAdd
        ans=ans and self.point[0]==pokemon.point[0] and self.point[1]==pokemon.point[1]
        if self.Edge==None:
            ans=ans and pokemon.Edge==None
        else:
            ans=ans and pokemon.Edge[0]==self.Edge[0] and self.Edge[1]==pokemon.Edge[1]
        return ans
    def SetEdge(self,Edge):
        self.Edge=Edge
    def GetPoint(self):
        return self.point
    def GetEdge(self):
        return self.Edge
    def SetPoint(self,point=()):
        self.point=point
    def __str__(self):
        return "{value: "+str(self.valu)+"edge: {"+str(self.Edge[0])+","+str(self.Edge[1])+"}"



