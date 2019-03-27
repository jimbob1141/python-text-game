from inventory import Inventory
class Rooms:
    def __init__(self):
        self.hallway_count = 0
        self.bathroom_count = 0
        self.adjacent = {
                "hallway": ["kitchen", "living room", "bedroom", "bathroom"],
                "bathroom": ["hallway"]}
        self.room_actions = {
                 "bathroom": ["inspect the bath", "rusty key"]}
        self.actions = ["check inventory"]
        return
    
    def hallway(room_count, p_invent):
        if room_count.hallway_count < 1:
          print("You find yourself in a hallway")
          print("You can't remember what happened")
          print("What will you do?")
          room_count.hallway_count = room_count.hallway_count + 1
        else:
          print("You return to the hallway")
        Rooms.list_contents("hallway", room_count, p_invent)
    
    def bathroom(room_count, p_invent):
        if room_count.bathroom_count < 1:
            print("You fumble around in the dark room")
            print("You eventually find turn the light on")
            print("There's a strange smell in the air")
        else:
            print("You enter the bathroom")
            print("There's a strange smell in the air")
            
                    
    def list_contents(room, room_count, p_invent, ):
        selector = []
        list_counter = 1
        for adjacent_room in room_count.adjacent[room]:
            print(str(list_counter) + ". Go to the " + adjacent_room)
            selector.append(adjacent_room)
            list_counter = list_counter + 1
        
        for action in room_count.actions:
            print(str(list_counter) + ". " + action)
            selector.append(action)
        
        while True:
            user_input = int(input())
            if user_input > len(selector) or user_input < 0:
                print("invalid number entered")
                print(len(selector))
                continue
            if selector[user_input - 1] in room_count.actions:
                function_name = selector[user_input - 1].replace(" ", "_")
                getattr(Inventory, function_name)(p_invent)
    