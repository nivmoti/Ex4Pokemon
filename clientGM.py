"""
@author AchiyaZigi
OOP - Ex4
Very simple GUI example for python client to communicates with the server and "play the game!"
"""
import math
from types import SimpleNamespace
from client import Client
import json
from pygame import gfxdraw
import pygame
from pygame import *
from buttom import Button
import math
from src import *
from src.Pokemon import Pokemon
from src.Agent import Agent

# init pygame
from src.control import control

WIDTH, HEIGHT = 1080, 720

# default port
PORT = 6666
# server host (default localhost 127.0.0.1)
HOST = '127.0.0.1'
pygame.init()

screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
clock = pygame.time.Clock()
pygame.font.init()

client = Client()
client.start_connection(HOST, PORT)



pokemons = client.get_pokemons()
pokemons_obj = json.loads(pokemons, object_hook=lambda d: SimpleNamespace(**d))
balba=pygame.image.load("charma.jpg")
ash=pygame.image.load("ash.jpg")


butt=pygame.image.load("buttom.jpg")



FONT = pygame.font.SysFont('Arial', 20, bold=True)
# load the json string into SimpleNamespace Object


graph_json = client.get_graph()
graph = json.loads(
    graph_json, object_hook=lambda json_dict: SimpleNamespace(**json_dict))

for n in graph.Nodes:
    x, y, _ = n.pos.split(',')
    n.pos = SimpleNamespace(x=float(x), y=float(y))

# get data proportions
min_x = min(list(graph.Nodes), key=lambda n: n.pos.x).pos.x
min_y = min(list(graph.Nodes), key=lambda n: n.pos.y).pos.y
max_x = max(list(graph.Nodes), key=lambda n: n.pos.x).pos.x
max_y = max(list(graph.Nodes), key=lambda n: n.pos.y).pos.y


def scale(data, min_screen, max_screen, min_data, max_data):
    """
    get the scaled data with proportions min_data, max_data
    relative to min and max screen dimentions
    """
    return ((data - min_data) / (max_data-min_data)) * (max_screen - min_screen) + min_screen


# decorate scale with the correct values

def my_scale(data, x=False, y=False):
    if x:
        return scale(data, 50, screen.get_width() - 50, min_x, max_x)
    if y:
        return scale(data, 50, screen.get_height()-50, min_y, max_y)


radius = 15
ash=pygame.image.load("ash.jpg")
balba=pygame.image.load("charma.jpg").convert_alpha()
butto=Button(10,10,butt,0.1)



# this commnad starts the server - the game is running now

"""
The code below should be improved significantly:
The GUI and the "algo" are mixed - refactoring using MVC design pattern is required.
"""
info = json.loads(client.get_info())
num_agents = info['GameServer']['agents']
for n in range(num_agents):
    name = "{\"id\":"+str(n)+"}"
    client.add_agent(name)
client.start()
d=int(client.time_to_end())
poke=json.loads(client.get_pokemons())
print(poke)
fuc=control(client)
time=float(client.time_to_end())
listOfTime=[]
count=0
while float(client.time_to_end()) >= 100.0:
    pokemons1 = json.loads(client.get_pokemons(),
                           object_hook=lambda d: SimpleNamespace(**d)).Pokemons
    pokemons = [p.Pokemon for p in pokemons1]
    for p in pokemons:
        x, y, _ = p.pos.split(',')
        p.pos = SimpleNamespace(x=my_scale(float(x), x=True), y=my_scale(float(y), y=True))
    agents = json.loads(client.get_agents(),
                        object_hook=lambda d: SimpleNamespace(**d)).Agents
    agents = [agent.Agent for agent in agents]
    for a in agents:
        x, y, _ = a.pos.split(',')
        a.pos = SimpleNamespace(x=my_scale(
            float(x), x=True), y=my_scale(float(y), y=True))
    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    # refresh surface
    screen.fill(Color(0, 0, 0))

    # draw nodes
    for n in graph.Nodes:
        x = my_scale(n.pos.x, x=True)
        y = my_scale(n.pos.y, y=True)

        # its just to get a nice antialiased circle
        gfxdraw.filled_circle(screen, int(x), int(y),
                              radius, Color(64, 80, 174))
        gfxdraw.aacircle(screen, int(x), int(y),
                         radius, Color(255, 255, 255))

        # draw the node id
        id_srf = FONT.render(str(n.id), True, Color(255, 255, 255))
        rect = id_srf.get_rect(center=(x, y))
        screen.blit(id_srf, rect)

        # draw edges
    for e in graph.Edges:
        # find the edge nodes
        src = next(n for n in graph.Nodes if n.id == e.src)
        dest = next(n for n in graph.Nodes if n.id == e.dest)

        # scaled positions
        src_x = my_scale(src.pos.x, x=True)
        src_y = my_scale(src.pos.y, y=True)
        dest_x = my_scale(dest.pos.x, x=True)
        dest_y = my_scale(dest.pos.y, y=True)

        # draw the line
        pygame.draw.line(screen, Color(61, 72, 126),
                         (src_x, src_y), (dest_x, dest_y))
    # draw agents
    for agent in agents:
        #pygame.draw.circle(screen, Color(122, 61, 23),
         #                  (int(agent.pos.x), int(agent.pos.y)), 10)
        ash=pygame.transform.scale(ash,(100,100))
        screen.blit(ash,(int(agent.pos.x), int(agent.pos.y)))
    # draw pokemons (note: should differ (GUI wise) between the up and the down pokemons (currently they are marked in the same way).
    for p in pokemons:
        pygame.draw.circle(screen, Color(0, 255, 255), (int(p.pos.x), int(p.pos.y)), 10)
        balba=pygame.transform.scale(balba,(100,100))
        screen.blit(balba,(int(p.pos.x),int(p.pos.y)))
    #    screen.blit(balba, int(p.pos.x), int(p.pos.y))
    if (butto.draw(screen)):
        client.stop()
        client.stop_connection()

    # update screen changes
    display.update()

    # refresh rate
    clock.tick(60)




    # choose next edge
    #'{"agent_id":0, "next_node_id":1}'.
    pokes=json.loads(client.get_pokemons())
    fuc.createPockemon(pokes)
    age = client.get_agents()
    fuc.updateAge(age)
    fuc.allocate()
    for a in fuc.listOfAgent:
        s = print(a.index)
        print(a.vertex)
        if a.dest == -1:
            d=a.getnext()
            if d!=-2:
                   dic = '{"agent_id":'+str(a.id) +', "next_node_id":'+str(d)+'}'
                   print(dic)
                   client.choose_next_edge(dic)
    client.move()
    age = client.get_agents()
    ans=fuc.updateAge(age)
    pokes = json.loads(client.get_pokemons())
    fuc.createPockemon(pokes)
    currtime = float(client.time_to_end())


print(client.get_info())
client.stop_connection()








# game over: