from pygame import K_ESCAPE
from Management.events import Stop
from Management.listener import Listener

class Quitter(Listener):
    
    """Extremely bare-bones game model which does nothing except quit if it
    receives a push of the ESC key.
    """
    
    def __init__(self, manager):
        self.manager = manager
        self.manager.register(self)
        
    def keydown(self, key):
        """Checks if the key pushed is the ESC key, and if it is, creates a
        Stop event.
        """
        if key == K_ESCAPE:
            self.manager.queueEvent( Stop() )