from src.Agent import Agent
from src.GraphAlgo import GraphAlgo
from src.Pokemon import Pokemon
from typing import List
from src.GraphAlgo import GraphAlgo
from src.Node import Node
from types import SimpleNamespace
from client import Client
import json
from pygame import gfxdraw
import pygame
from pygame import *
from src import *

class Gui:

    def scale(self,data, min_screen, max_screen, min_data, max_data):
        """
        get the scaled data with proportions min_data, max_data
        relative to min and max screen dimentions
        """
        return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen

    def my_scale(self,data, x=False, y=False):
        if x:
            return self.scale(data, 50,  self.screen.get_width() - 50, min_x, max_x)
        if y:
            return self.scale(data, 50, self.screen.get_height() - 50, min_y, max_y)
    def __init__(self,poke_list: List[Pokemon],agent_list: List[Agent],graph=GraphAlgo()):
        self.agent_list = agent_list
        self.graf=graph
        self.pokemons=poke_list

    def updateAgents(self,agent_list: List[Agent]):
        self.agent_list=agent_list
    def updatePokemons(self,poke_list: List[Pokemon]):
        self.pokemons=poke_list


    def plot_graph(self) -> None:
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
        FONT = pygame.font.SysFont('Arial', 20, bold=True)
        min_x = min(list(graph.Nodes), key=lambda n: n.pos.x).pos.x
        min_y = min(list(graph.Nodes), key=lambda n: n.pos.y).pos.y
        max_x = max(list(graph.Nodes), key=lambda n: n.pos.x).pos.x
        max_y = max(list(graph.Nodes), key=lambda n: n.pos.y).pos.y

        return None
