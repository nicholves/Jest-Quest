from NPC import *

class Blacksmith(NPC):


    def speakto(self):
        print("I am in desperate need of some iron from the mine. Get me some and i'll make you a performance sword")


    def receive(self, item):
        if item.name == "IRON":
            return "get sword"

        return None