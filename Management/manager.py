from weakref import WeakKeyDictionary
from twisted.internet.defer import Deferred
from listener import Listener

class Manager(object):

    """The manager object receives all the events and forwards them to the
    interested objects.
    """
    
    def __init__(self):
        self.listeners = WeakKeyDictionary()
        self.eventQueue = Deferred() # Uses a deferred object to handle the
                                     # queueing of events
        self.eventQueue.callback(1) # kick-off the queue on initialization
                                       # so it attempts to run the next job
                                       # whenever it can
    
    def register(self, listener):
        assert isinstance(listener, Listener), "Only classes inheriting from \
the Listener base-class can register with the manager as a listener"
        self.listeners[listener] = 1
        
    def queueEvent(self, event):
        self.eventQueue.addCallbacks(self.post, self.printError, (event,) )
    
    def post(self, __, event):
        """This method is designed to be queued in a deferred object, so its
        first parameter is ignored, and its return in None, because the return
        of a callback in a deferred is passed in as the first parameter of the
        next callback method, so posts can be chained together in the
        eventQueue deferred indefinitely."""
        for listener in self.listeners.keys():
            listener.getEvent(event)
        return 1
        
    def printError(self, fail):
        print fail.getTraceback()
        fail.trap(RuntimeError)