from NPC import *
from random import *

class Bellmaker(NPC):
    def __init__(self, name, location, comedy_resistance):
        self.name = name
        self.location = location
        self.comedy_resistance = comedy_resistance
        self.defeated = False
        self.received_bells = False


    def speakto(self):
        print("you look like you need some bells for your jester's hat. Just pay me 30 gold and they're yours")


    def pay(self, amount):
        if amount == 30 and not self.received_bells:
            received_bells = True
            return "give player bells"
        else:
            print("Pay me exactly 30 gold")
            return None


    def move(self, locations_masterlist):
        if randint(0,100) <= 20 and self.location.name == "FOUNTAIN":
            self.location = locations_masterlist["BELLMAKER'S STORE"]
            locations_masterlist["BELLMAKER'S STORE"].add_character(self)
            locations_masterlist["FOUNTAIN"].remove_character(self)
            
        elif randint(0,100) <= 20 and self.location.name == "BELLMAKER'S STORE":
            self.location = locations_masterlist["FOUNTAIN"]
            locations_masterlist["FOUNTAIN"].add_character(self)
            locations_masterlist["BELLMAKER'S STORE"].remove_character(self)
