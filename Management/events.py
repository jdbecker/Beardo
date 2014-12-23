class Event(object):
    
    """Super class for all event objects"""
    
    def __init__(self):
        """Generic event does nothing by default."""
        self.name = "Default Event"
    
    def __str__(self):
        return self.name
        
if __name__ == '__main__':
    e = Event()
    print e