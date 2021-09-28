class Player():
    def __init__(self, starting_location):
        self.inventory = []
        self.current_location = starting_location
        self.current_comedy = 5
        self.money = 0
    
    def __init__(self):
        self.inventory = []
        self.current_location = ""
        self.current_comedy = 5
        self.money = 0

    def describe_location(self):
        self.current_location.describe()

    def check_inventory(self):
        print("In my inventory I see: ")
        for item in inventory:
            print(item)

    def goto(self, destination):
        flag = False
        for connection in self.current_location.connections:
            try:
                if connection.name == destination.upper():
                    self.current_location = connection
                    return True
            except:
                print("I've never heard of a place called that")


        print("I don't know how to get there from where I am")
        print()

