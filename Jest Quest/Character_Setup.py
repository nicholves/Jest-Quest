from Characters.Bart import Bart
from Characters.Bellmaker import Bellmaker
from Characters.Blacksmith import Blacksmith
from Characters.Castle_Guard import Castle_Guard
from Characters.Chef import Chef
from Characters.Drunkman_Godfried import Drunkman_Godfried
from Characters.Gambler import Gambler
from Characters.King import King
from Characters.Miner import Miner
from Characters.Music_Store_Owner import Music_Store_Owner
from Characters.Ogre import Ogre
from Characters.Pinseller import Pinseller
from Characters.Servant_Girl import Servant_Girl
from Characters.Smuggler import Smuggler
from Characters.Tailor import Tailor
from Characters.TavernKeep import TavernKeep
from Characters.Witch import Witch







def Setup_Characters(people_masterlist):
    people_masterlist["BART"] = Bart("Bart", "BACK ALLEY", 25)
    people_masterlist["BELLMAKER"] = Bellmaker("Bellmaker", "BELLMAKER'S STORE", 10)
    people_masterlist["BLACKSMITH"] = Blacksmith("Blacksmith", "BLACKSMITH'S FORGE", 10)
    people_masterlist["CASTLE GUARD"] = Castle_Guard("Castle guard", "CASTLE GATES", 10)
    people_masterlist["CHEF"] = Chef("The Castle Chef", "CASTLE KITCHEN", 30)
    people_masterlist["DRUNKMAN GODFRIED"] = Drunkman_Godfried("Drunkman Godfried", "TAVERN", 20)
    people_masterlist["GAMBLER"] = Gambler("The gambler", "CASTLE DUNGEONS", 15)
    people_masterlist["KING"] = King("King Alfred", "THRONE ROOM", 125)
    people_masterlist["MINER"] = Miner("A soot covered miner", "IRON MINE", 15)
    people_masterlist["MUSIC STORE OWNER"] = Music_Store_Owner("The music store owner", "MUSIC STORE", 15)
    people_masterlist["OGRE"] = Ogre("A hideous ogre", "UNDER THE BRIDGE UNDER BRIDGE", 500)
    people_masterlist["PINSELLER"] = Pinseller("A comely old pinseller", "MARKET", 5)
    people_masterlist["SERVANT GIRL"] = Servant_Girl("A beutiful young servant girl", "CASTLE GARDENS", 70)
    people_masterlist["SMUGGLER"] = Smuggler("A dastardly Smuggler", "SMUGGLER'S HOUSE", 45)
    people_masterlist["TAILOR"] = Tailor("A young overworked tailor", "TAILOR'S HUT", 25)
    people_masterlist["TAVERN KEEP"] = TavernKeep("A chubby tavernkeep who's seen it all", "TAVERN", 55)
    people_masterlist["WITCH"] = Witch("A cackling evil old witch, covered in green pustules", "WITCH'S CAVE", 85)

