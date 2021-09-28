from NPC import *

class Witch(NPC):
    

    def speakto(self):
        print("HEHEHEHEEEHEHEH!!! Return me my gold and i'l enchant your tunic for you")

    def receive(self, item):
        if item.name == "PILE OF TREASURE":
            print("You are one smart gentleman hehehehe")
            return "enchant tunic"
        print("not what I wanted")
        return None

    