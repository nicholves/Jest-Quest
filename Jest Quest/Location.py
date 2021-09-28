class Location():
    def __init__(self, name, description, characters_within, items_within, connections, connection_descriptions):
        self.name = name
        self.description = description
        if characters_within == "":
            self.characters_within = None
        else:
            self.characters_within = characters_within
        if items_within == "":
            self.items_within = None
        else:
            self.items_within = items_within
        self.connections = connections
        self.connection_descriptions = connection_descriptions

    def describe(self):
        description = self.description.split("~")
        for line in description:
            print(line.replace(']', ','))
        if self.items_within != None:
            print("you can see the following items: ")
            for item in self.items_within:
                print("\t" + item.name)

        print()


        if not self.characters_within == None:
            print("The following people are here: ")
            for person in self.characters_within:
                person.describe()
            print()

        for connection in self.connection_descriptions.split("~"):
            print(connection)


    def fix_connections(self, locations_masterlist):
        if self.connections == None:
            return
        connections_splited = self.connections.split(";")
        self.connections = []
        for connect in connections_splited:
            try:
                self.connections.append(locations_masterlist[connect])
            except:
                pass


    def fix_itemswithin(self, items_masterlist):
        if self.items_within == None:
            return
        items_splitted = self.items_within.split(";")
        self.items_within = []
        for item in items_splitted:
            self.items_within.append(items_masterlist[item])

    def fix_characterswithin(self, people_masterlist):
        if self.characters_within == None:
            return
        people_splitted = self.characters_within.split(";")
        self.characters_within = []
        for character in people_splitted:
            self.characters_within.append(people_masterlist[character])


    def remove_item(self, item):
        self.items_within.remove(item)
        if len(self.items_within) == 0:
            self.items_within = None


    def add_item(self, itemname, items_masterlist):
        if self.items_within == None:
            self.items_within = [items_masterlist[itemname]]
        else:
            self.items_within.append(items_masterlist[itemname])

    def add_character(self, character):
        if self.characters_within == None:
            self.characters_within = [character]
        else:
            self.characters_within.append(character)

    def remove_character(self, character):
        self.characters_within.remove(character)

        if len(self.characters_within) == 0:
            self.characters_within = None