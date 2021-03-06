import random
import pandas as pd
from Data.Arrays.petArrays import petEmojis, petNatures
from Functions.dates import MDYtoDMY, getCurrentDate
from Functions.getUser import getUser
from Functions.length import dateDiff
from table2ascii import table2ascii as t2a, PresetStyle

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
    df.loc[len(df.index)] = [len(df.index), args[1], args[2].capitalize() + getPetEmoji(args[2]), getCurrentDate(), 0, random.choice(petNatures), getUser(author), 0, 0]
    df.at[len(df.index)-1,"Age"] = dateDiff(MDYtoDMY(df.at[len(df.index)-1, "Birthday"]), MDYtoDMY(getCurrentDate()))
    print(df)
    df.to_excel('Data/SaveFiles/Pets.xlsx', index=False)
    return getUser(author) + " has adopted " + args[1] + getPetEmoji(args[2])

def getTotalPets():
    df = pd.read_excel('Data/SaveFiles/Pets.xlsx')
    for i in range(len(df.index)):
         df.at[i,"Age"] = dateDiff(MDYtoDMY(df.iloc[i]["Birthday"]), MDYtoDMY(getCurrentDate()))
    df.to_excel('Data/SaveFiles/Pets.xlsx', index=False)
    return len(df.index)

def getPet(index):
    df = pd.read_excel('Data/SaveFiles/Pets.xlsx')
    start = MDYtoDMY(df.iloc[index]["Birthday"])
    end = MDYtoDMY(getCurrentDate())
    petArray = [df.iloc[index]["ID"],
        df.iloc[index]["Name"],
        df.iloc[index]["Type"],
        df.iloc[index]["Birthday"],
        df.iloc[index]["Age"],
        df.iloc[index]["Nature"],
        df.iloc[index]["Owner"],
        df.iloc[index]["FavFood"]
        ]
    return [petArray]

#header=["ID", "Name", "Type", "Birthday", "Age", "Nature", "FavFood", "Owner"]
def getAllPets():
    petArray = []
    for i in range(getTotalPets()):
        pet = getPet(i)
        petArray = petArray + pet
    return petArray

def printAllPets():
    output = t2a(
    header=["ID", "Name", "Type", "Birthday", "Age", "Nature", "Owner", "FavFood"],
    body=getAllPets(),
    )
    return output



