from Management.events import Stop
from Management.listener import Listener

class Console(Listener):
    
    """Simple object for catching message events and printing them to the
    console.
    """
    
    def __init__(self, manager):
        self.manager = manager
        self.manager.register(self)
        self.ticks = 0
    
    def printMessage(self, message):
        """Print given message to the console."""
        print message
        
    def tick(self):
        self.ticks += 1
        print "tick... #" + str(self.ticks)
        if self.ticks >= 10:
            self.manager.queueEvent( Stop() )