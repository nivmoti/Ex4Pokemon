import json
import math

from src import DiGraph
from src.Agent import Agent
from src.DiGraph import DiGraph
from src import GraphAlgo
from src.GraphAlgo import GraphAlgo
from src.Pokemon import Pokemon
import client
from client import Client


class control:
    def lineMagnitude(self,x1, y1, x2, y2):
        lineMagnitude = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))
        return lineMagnitude

    def DistancePointLine(self,px, py, x1, y1, x2, y2):
        # http://local.wasp.uwa.edu.au/~pbourke/geometry/pointline/source.vba
        LineMag = self.lineMagnitude(x1, y1, x2, y2)

        if LineMag < 0.00000001:
            DistancePointLine = 9999
            return DistancePointLine

        u1 = (((px - x1) * (x2 - x1)) + ((py - y1) * (y2 - y1)))
        u = u1 / (LineMag * LineMag)

        if (u < 0.00001) or (u > 1):
            # // closest point does not fall within the line segment, take the shorter distance
            # // to an endpoint
            ix = self.lineMagnitude(px, py, x1, y1)
            iy = self.lineMagnitude(px, py, x2, y2)
            if ix > iy:
                DistancePointLine = iy
            else:
                DistancePointLine = ix
        else:
            # Intersecting point is on the line, use the formula
            ix = x1 + u * (x2 - x1)
            iy = y1 + u * (y2 - y1)
            DistancePointLine = self.lineMagnitude(px, py, ix, iy)

        return DistancePointLine
    def distancePointfromLine(self,V={}, Pokemon=Pokemon(), Edge=()):
        p1 = V[Edge[0]].GetPoint()
        p2 = V[Edge[1]].GetPoint()
        p3 = Pokemon.GetPoint()
        d=self.DistancePointLine(p3[0],p3[1],p1[0],p1[1],p2[0],p2[1])
        return d
    def createPockemon(self,pokemons):
        # maxAgent = json.load(clinet.get_info())["GameServer"]["agents"]
        V = self.algo.graph.get_all_v()
        # while is begning
        min = float('inf')
        currEdge = None
        pokes = []
        for src in self.algo.graph.outEPokemon:
            for dest in self.algo.graph.outEPokemon[src]:
                self.algo.graph.outEPokemon[src][dest]=[]
        for n in range(len(pokemons["Pokemons"])):
            poke = Pokemon(pokemons["Pokemons"][n]["Pokemon"]["value"], pokemons["Pokemons"][n]["Pokemon"]["type"],pokemons["Pokemons"][n]["Pokemon"]["pos"])
            for a in V:
                for b in self.algo.graph.all_out_edges_of_node(a).keys():
                    if (pokemons["Pokemons"][n]["Pokemon"]["type"] == 1 and a <int(b) ) or (pokemons["Pokemons"][n]["Pokemon"]["type"] == -1 and a >int (b)):
                        Edge = (a,int(b))
                        d = self.distancePointfromLine(V, poke, Edge)
                        if (d<min):
                            currEdge = Edge
                            min=abs(d)
            poke.SetEdge(currEdge)
            self.algo.graph.addPockemon(poke)
            pokes.append(poke)

        return pokes
    def createAgent(self, file: str) -> dict:
        agents = []
        dict = json.loads(file)
        for n in range(len(dict["Agents"])):
            agent1 = Agent(dict["Agents"][n]["Agent"],self.algo)
            agents.append(agent1)
        return agents


    def updateAge(self, file: str) -> dict:
        agents = []
        dict = json.loads(file)
        if type(dict)==int:
            return False
        for n in range(len(dict["Agents"])):
          for agent in self.listOfAgent:
             agent.update(dict["Agents"][n]["Agent"])
        return True



    def __init__(self,agent,algo):
        self.listOfAgent=agent
        self.algo=algo

    def __init__(self,cl=Client()):
        self.algo = GraphAlgo()
        self.clinet = cl
        data=json.loads(self.clinet.get_graph())
        self.algo.load_from_json(data)
        self.graph=self.algo.get_graph()
        age=self.clinet.get_agents()
        self.listOfAgent = self.createAgent(age)

    # def keyyalla(self,section=Section()):
    #     return section.sumOfPekemons
    # def AgentINagentsReady(self):
    #     for agent in self.listOfAgent:
    #         if(agent.isCanGetSection):
    #             return agent
    #     return None
    def allocate(self):
        for agent in self.listOfAgent:
            if  agent.index==0 and agent.canGetVertex and agent.dest==-1:
                max = float('-inf')
                V = []
                isChange=False
                for src in self.algo.graph.outEPokemon:
                    for dest in self.algo.graph.outEPokemon[src]:
                        for i in range(len(self.algo.graph.outEPokemon[src][dest])):
                            if(self.algo.graph.outEPokemon[src][dest][i].isAdd==True):
                                continue
                            s = self.algo.shortest_path(agent.src,
                                                        self.algo.graph.outEPokemon[src][dest][i].Edge[0])
                            short = []
                            #print(self.algo.graph.outEPokemon[src][dest][i])
                            short.append(s[0] + self.algo.graph.outE[self.algo.graph.outEPokemon[src][dest][i].Edge[0]][
                                self.algo.graph.outEPokemon[src][dest][i].Edge[1]])
                            short1 = s[1]
                            short1.append(self.algo.graph.outEPokemon[src][dest][i].Edge[1])
                            short.append(short1)
                            sumOfPokemon = self.algo.graph.outEPokemon[src][dest][i].valu
                            for i in range(0, len(short[1]) - 1):
                                for j in range(0, len(self.algo.graph.outEPokemon[short[1][i]][short[1][i + 1]])):
                                    if self.algo.graph.outEPokemon[short[1][i]][short[1][i + 1]][j].isAdd == False:
                                        sumOfPokemon = sumOfPokemon + \
                                                       self.algo.graph.outEPokemon[short[1][i]][short[1][i + 1]][
                                                           j].valu
                            if sumOfPokemon > max and sumOfPokemon > 0.0:
                                max = sumOfPokemon
                                V = short[1]
                                isChange=True


                if isChange:
                    agent.setVertex(V)
                    for i in range(len(V) - 1):
                        for p in self.algo.graph.outEPokemon[V[i]][V[i + 1]]:
                            p.isAdd = True

    def move(self):
        poke =self.createPockemon(json.loads(self.clinet.get_pokemons()))
        # for p in poke:
        #     print(p.GetEdge())
        self.allocate()
        for agent in self.listOfAgent:
            if agent.canGetVertex and agent.index < len(agent.vertex)-1  and len(agent.vertex) != 0 and agent.dest==-1:
                agent.kilometePeSecond = agent.kilometePeSecond + \
                                         self.graph.all_out_edges_of_node(agent.vertex[agent.index])[
                                             agent.vertex[agent.index + 1]]
                agent.numberofvertex = agent.numberofvertex + 1
                agent.updateGet()
        for agent in self.listOfAgent:
            dic = []
            if agent.dest==-1:
                if agent.canGetVertex and agent.index < len(agent.vertex):
                    # print('{"agent_id":' + str(agent.id) + ', "next_node_id":' + str(agent.vertex[agent.index]) + '}')
                    dic.append('{"agent_id":' + str(agent.id) + ', "next_node_id":' + str(agent.getnext()) + '}')
                else:
                    dic.append('{"agent_id":' + str(agent.id) + ', "next_node_id":' +str(agent.getnext()) + '}')
                    if agent.time!=0 and self.clinet.time_to_end()-agent.time<1000:
                        if agent.numberofvertex == 10:
                            agent.canGetVertex = False
                    else:
                        agent.time = self.clinet.time_to_end()
                        agent.numberofvertex = 0
                        agent.kilometePeSecond = 0
            else:
                dic.append(-2)
        return dic
        # if not(self.listOFSection==None):
        #     self.listOFSection.sort(reverse=True, key=self.keyyalla)
        #     currAgent = None
        #     min = float('inf')
        #     for s in self.listOFSection:
        #         if s.isWasTaked == False:
        #             Agent = self.AgentINagentsReady()
        #             if (Agent != None):
        #                 for a in self.listOfAgent:
        #                     if (a.isCanGetSection and a.TimeToEnd(s) < min):
        #                         min = a.TimeToEnd(s)
        #                         Agent = a
        #                 s.isWasTaked = True
        #                 Agent.add(s)
        #             else:
        #                 break
    # def isInSection(self,poke):
    #     for j in range(0,len(self.listOFSection)):
    #         if self.listOFSection[j].state==-1 and poke.stat==-1:
    #             for j in range(self.listOFSection[j].start,self.listOFSection[j].end):
    #                 if poke[0]==self.S.listDownDi[j] and poke[1]==self.S.listDownDi[j+1]:
    #                     return j
    #         elif self.listOFSection[j].state==1 and poke.stat==1:
    #             for j in range(self.listOFSection[j].start, self.listOFSection[j].end):
    #                 if poke[0] == self.S.listupDi[j] and poke[1] == self.S.listupDi[j + 1]:
    #                     return j
    #     return -1

