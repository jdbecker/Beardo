from Management.manager import Manager
from Management.events import Message
from View.console import Console
from View.userDisplay import UserDisplay
from Controller.spinner import Spinner
from Controller.localInput import LocalInput
from Model.quitter import Quitter

manager = Manager()
con = Console(manager)
spin = Spinner(manager)
gui = UserDisplay(manager)
io = LocalInput(manager)
game = Quitter(manager)

manager.queueEvent(Message("Hello, World!"))
spin.start()