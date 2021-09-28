from NPC import *

class Music_Store_Owner(NPC):
    

    def speakto(self):
        print("Welcome! Welcome! Pay me 70 gold for a piccolo or 100 gold for a lute")


    def pay(self, amount):
        if amount == 100:
            return "give player lute"
        if amount == 70:
            return "give player piccolo"
        
        print("Pay me and exact amount of gold")
        return None