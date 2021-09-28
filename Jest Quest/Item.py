class Item():
    def __init__(self, name, comedic_value, description):
        self.comedy_value = comedic_value
        self.name = name
        self.description = description
        self.held = False

    def __str__(self):
        if self.held:
            return "A " + self.name + " with comedy value " + self.comedy_value
        else:
            return "A " + self.name

    def __rpr__(self):
        if self.held:
            return "A " + self.name + " with comedy value " + self.comedy_value
        else:
            return "A " + self.name



    def inspect(self):
        description = self.description.split("~")
        for line in description:
            print(line.strip())