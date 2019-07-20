import sys
from random import randint

import pygame
from pygame import gfxdraw

from Color import Color, get_rgb_value
from CSP import CSP
from Node import Node


class GUI():
    """
    GUI for displaying nodes, running CSP, and creating graph.
    """
    _line_width = 2
    _line_color = (255, 255, 255)
    _background_color = 50, 50, 50
    _size = 1920, 1080
    _circle_width = 10
    _font = "Verdana"
    _font_size = 30

    def __init__(self, nodes):
        """
        Creates a new GUI
        :param nodes: List of Node objects to refrence
        """
        self.nodes = nodes
        self.csp = CSP(self.nodes)
    
    def start(self):
        """
        Starts the GUI displaying the window.
        """
        pygame.init()
        pygame.font.init()
        font = pygame.font.SysFont(self._font, self._font_size)
        screen = pygame.display.set_mode(self._size)
        start_button = pygame.Rect(100, 100, 200, 50)
        reset_button = pygame.Rect(100, 300, 200, 50)

        while True:
            # Get events
            for event in pygame.event.get():
                x, y = pygame.mouse.get_pos()
                add_node = True
                
                # Quit GUI
                if event.type == pygame.QUIT: sys.exit()

                # Buttons
                if start_button.collidepoint((x, y)) and pygame.MOUSEBUTTONUP == event.type:
                    if len(self.nodes) > 0:
                        self.csp.performSearch(self.nodes[0])
                    add_node = False
                
                if reset_button.collidepoint((x, y)) and pygame.MOUSEBUTTONUP == event.type:
                    self.nodes = []
                    add_node = False
                
                # Add Node when mouse clicked
                if add_node and event.type == pygame.MOUSEBUTTONUP:
                    new_node = Node(None, x, y)
                    self.nodes.append(new_node)

                    # Add a random neighbor
                    if len(self.nodes) > 1:
                        for _ in self.nodes:
                             if randint(0,1):
                                random_neighbor = self.nodes[randint(0, len(self.nodes)-1)]
                                new_node.addNeighbor(random_neighbor)

            screen.fill(self._background_color)
            
            # Draw lines first
            for node in self.nodes:
                for neighbor in node.neighbors:
                    gfxdraw.line(screen, node._posX, node._posY, neighbor._posX, neighbor._posY, self._line_color)

            # Draw nodes second 
            for node in self.nodes:
                color = 0, 0 ,0
                vector = (node._posX, node._posY)
                if node._color is not None:
                    color = get_rgb_value(node._color)
                pygame.draw.circle(screen, color, vector, self._circle_width)

            # Draw Buttons
            pygame.draw.rect(screen, get_rgb_value(Color.GREEN), start_button)
            pygame.draw.rect(screen, get_rgb_value(Color.RED), reset_button)
            start_text = font.render('Start Search', False, (0, 0, 0))
            reset_text = font.render('Reset', False, (0, 0, 0))
            screen.blit(start_text,(105,105))
            screen.blit(reset_text,(145,305))
            
            
            pygame.display.flip()
