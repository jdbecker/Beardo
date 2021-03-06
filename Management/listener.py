from events import Event, Tick, Stop, Message, Keydown

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
        # For events going to debug listeners
        elif not isinstance(event, Tick):
            if "debug" in dir(self):
                self.debug(event)
            
        if isinstance(event, Tick): # Check if the event is a tick event
            if "tick" in dir(self): # check if the listener has a tick method
                self.tick()
        elif isinstance(event, Stop):
            if "stop" in dir(self):
                self.stop()
        elif isinstance(event, Keydown):
            if "keydown" in dir(self):
                self.keydown(event.key)
        elif isinstance(event, Message):
            if "message" in dir(self):
                self.message(event.message)
                
        else:
            raise Exception("Listener base-class doesn't support %s" % event)
            
if __name__ == "__main__":
    l = Listener()