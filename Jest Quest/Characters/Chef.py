from NPC import *

class Chef(NPC):
    

    def speakto(self):
        print("Are you a jester? I'd kill for a giggle good sir.")
        print("In the meantime, feel free to grab a sweetroll")


    def print_defeat(self, player):
        print(self.name + " defeated in comedic combat! You earned 50 gold")
        player.gold += 50