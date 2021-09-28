from random import *
from NPC import *

class Bart(NPC):
    

    def speakto(self):
        print("Oi Bruv! If ya fink you can get a laugh outta me! i'l give you a couple shillings!")


    def move(self, locations_masterlist):
        if randint(0,100) <=40 and self.location.name == "MARKET":
            self.location = locations_masterlist["BACK ALLEY"]
            locations_masterlist["BACK ALLEY"].add_character(self)
            locations_masterlist["MARKET"].remove_character(self)
        
        elif randint(0,100) <=40 and self.location.name == "BACK ALLEY":
            self.location = locations_masterlist["MARKET"]
            locations_masterlist["MARKET"].add_character(self)
            locations_masterlist["BACK ALLEY"].remove_character(self)

    def print_defeat(self, player):
        print(self.name + " defeated in comedic combat! You earned 40 gold")
        player.money += 40


    def receive(self, item):
        print("You ain't gonna best me with flattery")
        return None
