class Inventory:
    def __init__(self):
        self.items = {"Key" : "A rusty Key"}
        return

    def check_inventory(invent):
        for key, value in invent.items.items():
            print(key + ": " + value)
  
    def add_item(self, item, description):
        self[item] = description