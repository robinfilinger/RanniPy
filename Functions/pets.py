import random
import pandas as pd
from Data.Arrays.petArrays import petEmojis, petNatures
from Functions.dates import MDYtoDMY, getCurrentDate
from Functions.getUser import getUser
from Functions.length import dateDiff

def getPetEmoji(type):
    for i in range(len(petEmojis)):
        if petEmojis[i][0] == type.lower():
            return petEmojis[i][1]
    return "Not a valid type of pet!"

def isValidPetType(type):
    for i in range(len(petEmojis)):
        if petEmojis[i][0] == type.lower():
            return True
    return False

def adopt(args, author):
    df = pd.read_excel('Data/SaveFiles/Pets.xlsx')
    df.loc[len(df.index)] = [len(df.index), args[1], args[2].capitalize() + getPetEmoji(args[2]), getCurrentDate(), 0, random.choice(petNatures), 0, 0, getUser(author)]
    df.at[len(df.index)-1,"Age"] = dateDiff(MDYtoDMY(df.at[len(df.index)-1, "Birthday"]), MDYtoDMY(getCurrentDate()))
    print(df)
    df.to_excel('Data/SaveFiles/Pets.xlsx', index=False)
    return getUser(author) + " has adopted " + args[1] + getPetEmoji(args[2])

def getTotalPets():
    df = pd.read_excel('Data/SaveFiles/Pets.xlsx')
    return len(df.index)



