from src.GraphInterface import GraphInterface
from src.Node import Node


class DiGraph(GraphInterface):
    def __init__(self):
        self.v={}
        self.outE={}
        self.inE={}
        self.outEPokemon={}
        self.sizeOfE=0
        self.numberOfChanges=0
    def v_size(self) -> int:
        return len(self.v)
    def e_size(self) -> int:
        return self.sizeOfE
    def get_all_v(self) -> dict:
        return self.v
    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.inE[id1]

    def all_out_edges_of_node(self, id1: int) -> dict:
      return self.outE[id1]

    def get_mc(self) -> int:
       return self.numberOfChanges
    def addPockemon(self,pokemon):
        isExist = False
        for i in range(len(self.outEPokemon[pokemon.Edge[0]][pokemon.Edge[1]])):
            isExist=False
            if pokemon.equal(self.outEPokemon[pokemon.Edge[0]][pokemon.Edge[1]][i]):
                isExist=True
                break
        if isExist==False:
            pokemon.isAdd=False
            self.outEPokemon[pokemon.Edge[0]][pokemon.Edge[1]].append(pokemon)
    def removePockemon(self,pokemon):
        isExist = False
        for i in range(len(self.graph.outEPokemon[pokemon.Edge[0]][pokemon.Edge[1]])):
            isExist = False
            if pokemon.equal(self.graph.outEPokemon[pokemon.Edge[0]][pokemon.Edge[1]][i]):
                self.graph.outEPokemon[pokemon.Edge[0]][pokemon.Edge[1]].pop(i)
                isExist=True
                break
        return isExist
    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if((not id1 in self.v)or (not id2 in self.v)):
            return False
        if(id2 in self.outE[id1]):
            return False
        self.outE[id1][id2]=weight
        self.outEPokemon[id1][id2]=[]
        self.inE[id2][id1]=weight
        self.numberOfChanges=self.numberOfChanges+1
        self.sizeOfE=self.sizeOfE+1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if not self.v.get(node_id)==None:
            return False
        if(pos==None):
            p=None
        else:
            p=str(pos[0])+","+str(pos[1])+","+str(pos[2])
        n={"id":node_id,"pos":p}
        node=Node(n)
        self.v[node_id]=node
        self.inE[node_id]={}
        self.outE[node_id] = {}
        self.outEPokemon[node_id]={}
        self.numberOfChanges = self.numberOfChanges + 1
        return True
    def remove_node(self, node_id: int) -> bool:
        if  self.v.get(node_id)==None:
            return False
        self.v.pop(node_id)
        self.sizeOfE=self.sizeOfE-len(self.outE)-len(self.inE)
        self.numberOfChanges=self.numberOfChanges+len(self.outE[node_id])+len(self.inE[node_id])+1
        for k in self.outE[node_id]:
            self.inE[k].pop(node_id)
        for k in self.inE[node_id]:
            self.outE[k].pop(node_id)
        self.outE.pop(node_id)
        self.inE.pop(node_id)
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if(not node_id2 in self.outE[node_id1]):
            return False
        self.outE[node_id1].pop(node_id2)
        self.inE[node_id2].pop(node_id1)
        self.numberOfChanges=self.numberOfChanges+1
        self.sizeOfE=self.sizeOfE-1
        return True

    def __str__(self):
        data = {}
        data["Edges"] = []
        for src in self.outE.keys():
            if (len(self.outE[src]) != 0):
                for dest in self.outE[src].keys():
                    temp = {}
                    temp["src"] = src
                    temp["w"] = self.outE[src][dest]
                    temp["dest"] = dest
                    data["Edges"].append(temp)
        data["Nodes"] = []
        for node in self.v:
            temp = {}
            temp["pos"] = self.v[node].pos
            temp["id"] = self.v[node].getKey()
            data["Nodes"].append(temp)
        return data.__str__()
