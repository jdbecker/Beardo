from Management.events import Stop
from Management.listener import Listener

class Console(Listener):
    
    """Simple object for catching message events and printing them to the
    console.
    """
    
    def __init__(self, manager):
        self.manager = manager
        self.manager.register(self)
    
    def printMessage(self, message):
        """Print given message to the console."""
        print message

    def printDebug(self, eventName):
        print eventName
        
    def keydown(self, key):
        print "key:", str(key)