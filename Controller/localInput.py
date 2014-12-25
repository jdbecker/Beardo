import pygame

from Management.listener import Listener
from Management.events import Stop, Keydown

class LocalInput(Listener):
    
    """LocalInput handles the pygame event queue, and queues up handled events
    in the manager, where appropriate.
    """
    
    def __init__(self, manager):
        self.manager = manager
        self.manager.register(self)
        
    def tick(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.manager.queueEvent( Stop() )
            if event.type == pygame.KEYDOWN:
                self.manager.queueEvent( Keydown(event.key) )