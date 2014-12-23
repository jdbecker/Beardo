from twisted.internet import reactor
from twisted.internet.task import LoopingCall

class Spinner():
    
    """Acts as a twisted reactor object, with some application specific
    details.
    """
    
    def __init__(self, manager):
        self.tickCount = 0
        self.manager = manager
        FPS = 30
        interval = 1.0 / FPS
        tickLoop = LoopingCall(self.fireTick)
        tickLoop.start(interval)
        
    def fireTick(self):
        """Call once per frame to handle updates and refreshing."""
        self.tickCount += 1
        self.manager.tick()
        print self.tickCount
        if self.tickCount >= 10:
            self.stop()
        
    def start(self):
        reactor.run()
        
    def stop(self):
        reactor.stop()
        
if __name__ == '__main__':
    spinner = Spinner()
    spinner.start()