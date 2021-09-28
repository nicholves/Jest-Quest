from Player import *
from NPC import *
from Location import *
from Item import *
from Character_Setup import *
from random import *

locations_masterlist = {}

player = Player()

verbs = {
    "go, travel, follow, walk, run, march, stroll, move, venture" : "go",
    "attack, kill, murder, slay" : "kill",
    "pickup, pick up, collect, grab, pull, take" : "pickup",
    "engage, make, jest, joke" : "jest",
    "inspect, examine" : "inspect",
    "speakto, speak to, talk, talk to, converse" : "talk",
    "look" : "look",
    "gold, money, wallet" : "check gold",
    "pay" : "pay",
    "give" : "give",
    "inventory" : "inventory",
    "help" : "help"
    }

ignoreable_words = "to,the,back,our,my,do,with"

people_masterlist = {}

items_masterlist = {}

score = 0

helptext = "Some commands you could try: wallet, inventory, look, inspect, pickup, go, pay, give, inventory"


def init():
    load_locations(locations_masterlist)
    load_items(items_masterlist)
    load_characters(people_masterlist)
    for location in locations_masterlist:
        locations_masterlist[location].fix_connections(locations_masterlist)
        locations_masterlist[location].fix_characterswithin(people_masterlist)
        locations_masterlist[location].fix_itemswithin(items_masterlist)

    for character in people_masterlist:
        people_masterlist[character].fix_location(locations_masterlist)

    player.current_location = locations_masterlist["UPSTAIRSBEDROOM"]


def jest(player, NPC):
    resistance = NPC.comedy_resistance
    last_item_used = ""
    counter = 1
    print("Engaging in jesting combat against: " + NPC.name)
    print()
    while counter <=3:
        print("Current base jesting stat is: ", end="")
        print(player.current_comedy)
        print()
        print(NPC.name + " has resistance "  + str(resistance))
        print()
        print()
        print("Choose an item to use from your inventory or say 'NONE' to use base jesting stat only")
        print("USABLE INVENTORY ITEMS:")
        print()
        for item in player.inventory:
            if int(item.comedy_value) != 0 and item.name != last_item_used:
                print(item)
                print()

        selected = input("What do you choose to use? ")

        if selected.upper() != "NONE":
            flag = False
            try:
                for i in range (0, len(player.inventory)):
                    for word in selected.upper().split(" "):
                        if word in player.inventory[i].name:
                            if player.inventory[i].comedy_value == 0:
                                print("not possible")
                                continue
                            selected = player.inventory[i]
                            flag = True
                            break
                    if flag:
                        break
            except:
                print("not possible")
                continue

            if selected.name == last_item_used:
                print("not possible")
                continue

            try:
                print("this will do between " + str((float(selected.comedy_value)*0.75//1 + player.current_comedy)) + " and " + str((float(selected.comedy_value)*1.25//1 + player.current_comedy)) + " comedy damage to enemy's resistance.")
            except:
                print("not possible")
                continue
            choice = input("Are you sure you want to use this item? (y/n) ")

            if choice.lower() == "n":
                print()
                continue

            elif choice.lower() == "y":
                damage = randint(float(selected.comedy_value)*0.75//1 + player.current_comedy, float(selected.comedy_value)*1.25//1 + player.current_comedy)
                if last_item_used == "FLINT AND STEEL" and selected.name == "PINS":
                    damage*= 2
                resistance -= damage
                print()
                print("Dealt " + str(damage) + " points of comedy")
                print()
                counter+= 1
                last_item_used = selected.name
                if resistance <= 0:
                    NPC.defeated = True
                    NPC.print_defeat(player)
                    return

        else:
            print("this will do between " + str((player.current_comedy)) + " and " + str((player.current_comedy)) + " comedy damage to enemy's resistance.")
            choice = input("Are you sure you want to use this item? (y/n) ")

            if choice.lower() == "n":
                print()
                continue

            elif choice.lower() == "y":
                damage = randint(player.current_comedy, player.current_comedy)
                resistance -= damage
                print()
                print("Dealt " + str(damage) + " points of comedy")
                counter+= 1
                if resistance <= 0:
                    NPC.defeated = True
                    NPC.print_defeat(player)
                    return
            



    
    print("You lose!!!")
    print("better luck next time")
    print()




def load_items(items_masterlist):
    file = open("items.csv", "r")
    for line in file:
        line = line.split(",")
        items_masterlist[line[0]] = Item(line[0], line[1], line[2])

    file.close()

def load_characters(people_masterlist):
    Setup_Characters(people_masterlist)
    

def load_locations(locations_masterlist):
    file = open("locations.csv", "r")
    for line in file:
        line = line.split(",")
        locations_masterlist[line[0]] = Location(line[0], line[1], line[2], line[3], line[4], line[5])

    file.close()

def do_something(input_text, score):
    if input_text == "exit":
        quit(0)


    for i in range (5):
        print()
    input_text = input_text.split(" ")
    for word in input_text:
        word.strip()
        word.strip(",.")


    flag = False
    for word in input_text:
        if flag:
            break
        if word in ignoreable_words:
            continue
        for key in verbs:
            if word.lower() in key:
                syn_verb = verbs[key]
                flag = True
                break

    print()
    if syn_verb == "go":
        flag = False
        previous_word = ""
        for word in input_text:
            if word.lower() in ignoreable_words:
                continue
            if word.upper() == "CASTLE":
                    continue
            if word.upper() == "BRIDGE":
                if previous_word not in "UNDERNEATH":
                    player.goto("BRIDGE")
                    player.describe_location()
                    flag = True
                    break
            for key in locations_masterlist:
                if word.upper() in key:
                    if player.goto(key):
                        player.describe_location()
                        flag = True
                        break
            previous_word = word
            if flag:
                break
        for character in people_masterlist:
            people_masterlist[character].move(locations_masterlist)
        if flag == False:
            print("not possible")
            return
        return





    elif syn_verb == "look":
        print()
        player.describe_location()






    elif syn_verb == "check gold":
        print()
        print("You have : " + str(player.money) + " gold currently")





    elif syn_verb == "inventory":
        print()
        if len(player.inventory) == 0:
            print("Your inventory is empty")
            return
        print("Inventory: ")
        for item in player.inventory:
            print(item)







    elif syn_verb == "kill":
        print()
        print("Killing people would probably not help your chances with the king")








    elif syn_verb == "pickup":
        try:
            if player.current_location.items_within == None:
                print("Not possible")
                return
        except:
            print("Not possible")
            return
        print()
        for word in input_text:
            if word.lower() in ignoreable_words:
                continue
            flag = False
            for i in range (0, len(player.current_location.items_within)):
                if word.upper() in player.current_location.items_within[i].name:
                    item = player.current_location.items_within[i]
                    item.held = True
                    player.inventory.append(item)
                    print("successfully picked up " + item.__str__())
                    flag = True
                    break
            
            if flag:
                player.current_location.remove_item(item)
                if item.name == "TORCH":
                    score+= 1
                    print("all of a sudden you feel the ground shaking...")
                    print("an entrace has opened to the witch's cave")
                    locations_masterlist["FOUNTAIN"].connections.append(locations_masterlist["WITCH'S CAVE"])
                    locations_masterlist["FOUNTAIN"].connection_descriptions+= "~There is also the dark entrance to the witch's cave"
                return

        print("You are not sure how to do that")


    elif syn_verb == "talk":
        try:
            if player.current_location.characters_within == None:
                print("Not possible")
                return
        except:
            print("Not possible")
            return

        for word in input_text:
            if word.lower() in ignoreable_words:
                continue
            for person in player.current_location.characters_within:
                if word.upper() in person.name.upper():
                    person.speakto()
                    break








    elif syn_verb == "pay":
        try:
            if player.current_location.characters_within == None:
                print("Not possible")
                return
        except:
            print("Not possible")
            return
        flag = False
        amount = 0
        target = None
        for word in input_text:
            if flag:
                break
            if word.lower() in ignoreable_words:
                continue
            for person in player.current_location.characters_within:
                if flag:
                    break
                if word.upper() in person.name.upper():
                    for word in input_text:
                        try:
                            amount = int(word)
                            target = person
                            flag = True
                            break
                        except:
                            continue
                    
        if player.money - amount >= 0:
            return_value = target.pay(amount)
            player.money-= amount
        else:
            print("not possible")
            return





    elif syn_verb == "inspect":
        
        print()
        for word in input_text:
            if word.lower() in ignoreable_words:
                continue
            flag = False
            try:
                for i in range (0, len(player.current_location.items_within)):
                    if word.upper() in player.current_location.items_within[i].name:
                        player.current_location.items_within[i].inspect()
                        return
            except:
                pass

            try:
                for i in range (0, len(player.inventory)):
                    if word.upper() in player.inventory[i].name:
                        player.inventory[i].inspect()
                        return

            except:
                pass


        print("no item found with this name")
        return




    elif syn_verb == "give":
        try:
            if player.current_location.characters_within == None:
                print("Not possible")
                return
        except:
            print("Not possible")
            return
        item = ""
        for word in input_text:
            if word.lower() in ignoreable_words:
                continue
            for person in player.current_location.characters_within:
                if word.upper() in person.name.upper():
                    for word in input_text:
                        for item in player.inventory:
                            if word.upper() in item.name:
                                item2give = item

                                return_value = person.receive(item2give)
                                if return_value != None:
                                    player.inventory.remove(item)
                                break


    elif syn_verb == "jest":
        try:
            if player.current_location.characters_within == None:
                print("Not possible")
                return
        except:
            print("Not possible")
            return
        for word in input_text:
            if word.lower() in ignoreable_words:
                continue
            for person in player.current_location.characters_within:
                if word.upper() in person.name.upper():
                    if not person.defeated:
                        jest(player, person)
                    else:
                        print("character already defeated!")
                        continue

    elif syn_verb == "help":
        print(helptext)



    try:
        if return_value == None:
            return
        
        elif return_value == "give player bells":
            player.inventory.append(items_masterlist["BELLS"])
            player.inventory[-1].held = True
            print("you received bells!")
            score +=1

        elif return_value == "give player pins":
            player.inventory.append(items_masterlist["PINS"])
            player.inventory[-1].held = True
            print("you received juggling pins!")
            score += 1


        elif return_value == "get sword":
            player.inventory.append(items_masterlist["DUMMY SWORD"])
            player.inventory[-1].held = True
            print("you received a dummy sword!")
            score += 1

        elif return_value == "open castle":
            locations_masterlist["CASTLE GATES"].connections.append(locations_masterlist["CASTLE COURTYARD"])
            locations_masterlist["CASTLE GATES"].connection_descriptions = "From these gates you could return to the city market.~ There is also a path to the back alley of Voterdame~Since you have been granted acess to the castle you can head into the courtyard"
            print("You have been granted acess to the castle courtyard")
            score+= 1

        elif return_value == "give player lute":
            player.inventory.append(items_masterlist["LUTE"])
            player.inventory[-1].held = True
            print("you received a lute!")
            score += 1

        elif return_value == "give player piccolo":
            player.inventory.append(items_masterlist["PICCOLO"])
            player.inventory[-1].held = True
            print("you received a piccolo!")
            score +=1

        elif return_value == "treasure available":
            locations_masterlist["UNDER THE BRIDGE UNDER BRIDGE"].add_item("PILE OF TREASURE", items_masterlist)
            print("treasure can now be collected!")
            score+= 1

        elif return_value == "receive hat":
            player.inventory.append(items_masterlist["FOOL'S CAP"])
            player.inventory[-1].held = True
            print("you received the fool's cap")
            score += 1

        elif return_value == "enchant tunic":
            player.inventory.append(items_masterlist["MAGIC TUNIC"])
            player.inventory[-1].held = True
            print("you received an enchanted tunic! (base comedy + 20)")
            player.current_comedy += 20
            score += 1
        print()
    
    except:
        pass




if __name__ == "__main__":
    init()

    print(helptext)
    print()
    print("you awaken in...", end="")
    player.describe_location()
    while not people_masterlist["KING"].defeated:
        try:
            print()
            do_something(str(input("What shall you do? ")).strip(), score)
        except:
            print("You try and think of what to do but you lose your train of thought.")
            continue

    score += 1
    print("Congratulations you've earned your spot as court jester to King Alfred!")
    print("Score: " + str(score))