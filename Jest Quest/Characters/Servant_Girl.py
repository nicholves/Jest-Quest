from random import *
from NPC import *

class Servant_Girl(NPC):

    def speakto(self):
        if self.defeated == False:
            print("Thank you for the laughs")
        else:
            print("Are you funny? I'd love to hear a joke")


    def move(self, locations_masterlist):
        if randint(0,100) <= 10 and self.location.name == "UNREACHABLE":
            self.location = locations_masterlist["CASTLE GARDENS"]
            locations_masterlist["CASTLE GARDENS"].add_character(self)
            locations_masterlist["UNREACHABLE"].remove_character(self)
            
        elif randint(0,100) <= 10 and self.location.name == "CASTLE GARDENS":
            self.location = locations_masterlist["UNREACHABLE"]
            locations_masterlist["UNREACHABLE"].add_character(self)
            locations_masterlist["CASTLE GARDENS"].remove_character(self)
                    

    def print_defeat(self, player):
        print(self.name + " defeated in comedic combat! You earned 60 gold")
        player.money += 60

    def receive(self, item):
        print("oh no sorry! We aren't suposed to accept gifts")
        return None