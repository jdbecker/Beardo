class Event(object):
    """Super-class for all event objects"""
    def __init__(self):
        """Generic event does nothing by default."""
        self.name = "Default_Event"
    def __str__(self):
        return self.name

class Tick(Event):
    """Inherits only from Event. Read by any listener that keeps track of, or
    updates in response to, the passage of time.
    """
    def __init__(self):
        self.name = "Tick_Event"
        
class Message(Event):
    """An event which contains the string attribute 'message'."""
    def __init__(self, message):
        self.name = "Message_Event"
        self.message = message
        
class Stop(Event):
    """A Stop event is created to signal the stoppage of the program."""
    def __init__(self):
        self.name = "Stop_Event"

if __name__ == '__main__':
    e = Tick()
    print isinstance(e, Tick)