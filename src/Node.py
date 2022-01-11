class Node:

    def __init__(self, node={}):
        self.id = int(node["id"])
        if( node["pos"]==None):
            self.pos=None
        else:
            self.pos= node["pos"]
            arr = node["pos"].split(",")
            self.x = float(arr[0])
            self.y = float(arr[1])
            self.z = float(arr[2])
        self.d=float('inf')
        self.dadi=None

    def copy(self, node):
        self.x = node.x
        self.y = node.y
        self.z = node.z
        self.id = node.id

    def equal(self, node):
        if node==None:
            return False
        if self.x == node.x and self.y == node.y and self.z == node.z and self.id == node.id:
            return True
        else:
            return False


    def getKey(self):
        return self.id

    def setKey(self, ID):
        self.id = ID

    def getx(self):
        return self.x

    def setx(self, X):
        self.x = X

    def gety(self):
        return self.y

    def sety(self, Y):
        self.y = Y

    def getz(self):
        return self.z

    def setz(self, Z):
        self.z = Z
    def GetD(self):
        return self.d
    def setD(self,d):
        self.d=d
    def getDadi(self):
        return self.dadi
    def setDadi(self,u):
        self.dadi=u
    def __repr__(self):
         return "{'pos': "+str(self.pos)+", 'id': "+str(self.id)+" }"
    def GetPoint(self):
        return (self.x,self.y)