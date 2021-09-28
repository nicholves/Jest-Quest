from NPC import *

class Drunkman_Godfried(NPC):


    def speakto(self):
        print("Make me laugh funnnnnnnnyyy man....")


    def print_defeat(self, player):
        print(self.name + " defeated in comedic combat! You earned 40 gold")
        player.money += 40
