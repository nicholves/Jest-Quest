from NPC import *

class Pinseller(NPC):

    def speakto(self):
        print("Hey boy, if you pay me 60 gold I will give you some juggling pins. You look like you might need them")


    def print_defeat(self, player):
        print(self.name + " defeated in comedic combat! You earned 10 gold")
        player.money += 10

    def receive(self, item):
        print("Pay me dear boy. I'm not accepting gifts")
        return None


    def pay(self, amount):
        if amount == 60:
            return "give player pins"
        else:
            print("Pay me exactly 60 gold boy.")
            return None