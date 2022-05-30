from Data.Arrays.petArrays import petEmojis

def findOwner(petOwner):
    if petOwner == "robinfilinger":
        return "Riccardo"
    elif petOwner == "danni876":
        return "Danni"

def getPetEmoji(type):
    for i in range(len(petEmojis)):
        if petEmojis[i][0].lower() == type:
            return petEmojis[i][1]
    return "Not a valid type of pet!"