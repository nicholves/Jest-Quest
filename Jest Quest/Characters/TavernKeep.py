from NPC import *
from random import *

class TavernKeep(NPC):

    def speakto(self):
        randomnum = randint(0,100)
        if randomnum < 33:
            print("Hey, if you go to the bridge and go underneath there is some treasure hidden there")

        elif randomnum > 33 and randomnum <66:
            print("If you grab the torch at the fountain a path will open to a witch's cave")

        else:
            print("The smuggler has connections everywhere.... Both literally and physically. I know for sure he's got a tunnel to the back alleys")


    def print_defeat(self, player):
        print(self.name + " defeated in comedic combat! You earned 60 gold")
        player.money += 60