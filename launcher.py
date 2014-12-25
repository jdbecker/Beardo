from Management.manager import Manager
from Management.events import Message, Stop, Tick
from View.console import Console
from View.userDisplay import UserDisplay
from Controller.spinner import Spinner
from Controller.localInput import LocalInput

manager = Manager()
con = Console(manager)
spin = Spinner(manager)
gui = UserDisplay(manager)
io = LocalInput(manager)

manager.queueEvent(Message("Hello, World!"))
spin.start()