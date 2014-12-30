import pygame

from Management.listener import Listener

class UserDisplay(Listener):
    
    """Uses a pygame display object to present a human user with a GUI."""
    
    def __init__(self, manager):
        self.manager = manager
        pygame.init()
        pygame.display.set_mode((800,600), )#pygame.FULLSCREEN)