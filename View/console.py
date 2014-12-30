from Management.listener import Listener

class Console(Listener):
    
    """Simple object for catching message events and printing them to the
    console.
    """
    
    def __init__(self, manager):
        self.manager = manager
        self.manager.register(self)
    
    def message(self, message):
        """Print given message to the console."""
        print message

    def debug(self, event):
        print event
        
    def keydown(self, key):
        print "key:", str(key)