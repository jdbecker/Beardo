from events import Event, Tick, Stop, Message

class Listener(object):
    
    """Listener is an interface to be inherited by any object which will be
    receiving messages from the manager.
    """
    
    def __init__(self):
        """Listener is an abstract interface, and should not be instantiated."""
        raise Exception("Listener is an abstract interface. Inheriting classes \
must overrde __init__ method.")
                         
    def getEvent(self, event):
        if not isinstance(event, Event):
            raise Exception("getEvent only accepts Event objects")
            
        if isinstance(event, Tick): # Check if the event is a tick event
            if "tick" in dir(self): # check if the listener has a tick method
                self.tick()
        elif isinstance(event, Stop):
            if "stop" in dir(self):
                self.stop()
        # Debug events
        elif isinstance(event, Message):
            if "printMessage" in dir(self):
                self.printMessage(event.message)
                
        else:
            raise Exception("Listener base-class doesn't support %s" % event)
            
if __name__ == "__main__":
    l = Listener()