from NPC import *

class Gambler(NPC):

    def speakto(self):
        print("Hey buddy, I know you're a jester so if you're looking for some cards go to the smugglers house by the fountain outside town")
        print("there is a tunnel there connecting to my cell where I will leave you a deck")


    def print_defeat(self, player):
        print(self.name + " defeated in comedic combat! You earned nothing")

    def receive(self, item):
        print("I can't recieve gifts here buddy, this is prison")
        return None


    