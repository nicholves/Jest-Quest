from NPC import *

class Ogre(NPC):

    def speakto(self):
        if self.defeated == False:
            print("GRRRRRRRRRRRRR!!! Me vewy vewy Hungry. BAAAAAAA!!!!!")
        else:
            print("Dank you wittle man!")


    def receive(self, item):
        if item.name == "SWEETROLL":
            self.defeated = True
            print("By de gods dank you! Take my tweasure wittle man")
            return "treasure available"
        return None


    