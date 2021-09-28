from NPC import *

class Castle_Guard(NPC):
    def __init__(self, name, location, comedy_resistance):
        self.name = name
        self.location = location
        self.comedy_resistance = comedy_resistance
        self.defeated = False
        self.speech = "Dear sir, if you have a poster inviting you in please give it to me now"

    def speakto(self):
        print(self.speech)

    def receive(self, item):
        if item.name == "POSTER":
            speech = "You have been granted access to the castle good sir"
            return "open castle"
        return None

