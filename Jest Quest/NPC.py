class NPC():
    def __init__(self, name, location, comedy_resistance):
        self.name = name
        self.location = location
        self.comedy_resistance = comedy_resistance
        self.defeated = False

    def move(self, locations_masterlist):
        pass
        
    def speakto(self):
        pass

    def receive(self, item):
        print("not possible")
        return None

    def pay(self, amount):
        print("Not possible")
        return None

    def print_defeat(self, player):
        print(self.name + " defeated in comedic combat!")

    def describe(self):
        print(self.name)


    def fix_location(self, locations_masterlist):
        self.location = locations_masterlist[self.location]