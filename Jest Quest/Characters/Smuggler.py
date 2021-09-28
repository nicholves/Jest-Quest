from NPC import *

class Smuggler(NPC):


    def speakto(self):
        print("Greetings! I've been expecting you (don't ask how). Head through the tunnel to the gambler's cell and go get some cards")

    def print_defeat(self, player):
        print(self.name + " defeated in comedic combat! You earned 20 gold")
        player.money += 20

