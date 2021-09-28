from NPC import *

class Tailor(NPC):
    def __init__(self, name, location, comedy_resistance):
        self.name = name
        self.location = location
        self.comedy_resistance = comedy_resistance
        self.defeated = False
        self.received = 0


    def speakto(self):
        print("If you can get me some cotton and some bells I will make you a fools hat")


    def receive(self, item):
        if item.name == "BELLS":
            print("Thank you sir")
            self.received += 1
            if self.received == 2:
                return "receive hat"
            return "remove item"
            
        if item.name == "COTTON":
            print("Thank you sir")
            self.received += 1
            if self.received == 2:
                return "receive hat"
            return "remove item"

        return None