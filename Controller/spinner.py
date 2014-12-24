from twisted.internet import reactor
from twisted.internet.task import LoopingCall
from Management.listener import Listener
from Management.events import Tick

class Spinner(Listener):
    
    """Acts as a twisted reactor object, with some application specific
    details.
    """
    
    def __init__(self, manager):
        print "starting spinner..."
        self.manager = manager
        self.manager.register(self)
        
    def fireTick(self):
        """Call once per frame to handle updates and refreshing."""
        self.manager.queueEvent(Tick())
        
    def start(self):
        FPS = 30
        interval = 1.0 / FPS
        tickLoop = LoopingCall(self.fireTick)
        tickLoop.start(interval)
        reactor.run()
        
    def stop(self):
        reactor.stop()
        
if __name__ == '__main__':
    spinner = Spinner()
    spinner.start()