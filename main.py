from inventory import Inventory
from rooms import Rooms

def startGame():
    p_invent = Inventory()
    room_count = Rooms()
    Rooms.hallway(room_count, p_invent)

startGame()
    