import copy

from src.DiGraph import DiGraph
class FWA:
    def __init__(self,gra):
        self.gra=DiGraph()
        self.gra=copy.deepcopy(gra)
        self.keys=self.gra.v.keys()
        self.v=self.gra.get_all_v()
        self.mat = []
        self.next=[]
        for i in self.keys:
            rowList = []
            rownNxt=[]
            for j in self.keys:
                # you need to increment through dataList here, like this:
                if j in self.gra.all_out_edges_of_node(i) :
                 rowList.append(self.gra.all_out_edges_of_node(i)[j])
                 rownNxt.append(j)
                elif i== j:
                    rowList.append(0)
                    rownNxt.append(0)
                else:
                    rowList.append(float('inf'))
                    rownNxt.append(-1)
            self.mat.append(rowList)
            self.next.append(rownNxt)
        self.floydWarshall()
    def floydWarshall(self):
        for k in self.keys:
            for i in self.keys:
                for j in self.keys:
                    if self.mat[i][j]>self.mat[i][k]+self.mat[k][j]:
                        self.mat[i][j]=self.mat[i][k]+self.mat[k][j]
                        self.next[i][j]=self.next[i][k]
    def center(self):
        e=[]
        c=[]
        rad=float('inf')
        for i in self.keys:
            e.append(0)
        for j in self.keys:
            for k in self.keys:
             e[j]=max(e[j],self.mat[j][k])
        for s in self.keys:
            rad=min(rad,e[s])
        for u in self.keys:
            if rad==e[u]:
                c.append(u)
        return (c[0],rad)
    def Connected(self):
        for i in self.keys:
            for j in self.keys:
                if self.mat[i][j]>=float('inf'):
                    return False

        return True
    def shortPath(self,u,v):
        if self.mat[u][v] >=float('inf'):
            return float('inf')
        else:
            return self.mat[u][v]
    def constructPath(self,u,v):
        c=[]
        if self.next[u][v]== -1:
            return []
        else:
            c.append(self.v[c])
            while not u==v:
                u=self.next[u][v]
                if self.next[u][v] == -1:
                    return []
                else:
                 c.append(self.v[u])
            return c





