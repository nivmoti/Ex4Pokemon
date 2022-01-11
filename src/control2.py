from src.Pokemon import Pokemon
import math
class control2:
    def _init_(self, agent, algo):
        self.listOfAgent = agent
        self.algo = algo

    def lineMagnitude(self, x1, y1, x2, y2):
        lineMagnitude = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))
        return lineMagnitude

    def DistancePointLine(self, px, py, x1, y1, x2, y2):
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

    def distancePointfromLine(self, V={}, Pokemon=Pokemon(), Edge=()):
        p1 = V[Edge[0]].GetPoint()
        p2 = V[Edge[1]].GetPoint()
        p3 = Pokemon.GetPoint()
        d = self.DistancePointLine(p3[0], p3[1], p1[0], p1[1], p2[0], p2[1])
        return d

    def createPockemon(self, pokemons):
        # maxAgent = json.load(clinet.get_info())["GameServer"]["agents"]
        V = self.algo.graph.get_all_v()
        # while is begning
        min = float('inf')
        currEdge = None
        pokes = []
        for src in self.algo.graph.outEPokemon:
            for dest in self.algo.graph.outEPokemon[src]:
                self.algo.graph.outEPokemon[src][dest] = []
        for n in range(len(pokemons["Pokemons"])):
            poke = Pokemon(pokemons["Pokemons"][n]["Pokemon"]["value"], pokemons["Pokemons"][n]["Pokemon"]["type"],
                           pokemons["Pokemons"][n]["Pokemon"]["pos"])
            for a in V:
                for b in self.algo.graph.all_out_edges_of_node(a).keys():
                    if (pokemons["Pokemons"][n]["Pokemon"]["type"] == 1 and a < int(b)) or (
                            pokemons["Pokemons"][n]["Pokemon"]["type"] == -1 and a > int(b)):
                        Edge = (a, int(b))
                        d = self.distancePointfromLine(V, poke, Edge)
                        if (d < min):
                            currEdge = Edge
                            min = abs(d)
            poke.SetEdge(currEdge)
            self.algo.graph.addPockemon(poke)
            pokes.append(poke)

        return pokes

    def allocate(self):
        for agent in self.listOfAgent:
            if agent.index == 0 and agent.canGetVertex and agent.dest == -1:
                max = float('-inf')
                V = []
                isChange = False
                for src in self.algo.graph.outEPokemon:

                    for dest in self.algo.graph.outEPokemon[src]:

                        for i in range(len(self.algo.graph.outEPokemon[src][dest])):

                            if (self.algo.graph.outEPokemon[src][dest][i].isAdd == True):
                                continue
                            s = self.algo.shortest_path(agent.src,
                                                        self.algo.graph.outEPokemon[src][dest][i].Edge[0])
                            short = []
                            # print(self.algo.graph.outEPokemon[src][dest][i])
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
                                isChange = True