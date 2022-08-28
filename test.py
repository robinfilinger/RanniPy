import pandas as pd
from Functions.countdowns import addCountdown, isCountdownValid, timeUntil, getTotalCountdowns
import re

from Functions.pets import getPet, getTotalPets
from Functions.pokemon import pokedexInfo

#args = ["command", "Together", "07/02/10", "9:30", "PM"]
#print(addCountdown(args)

#time = timeUntil("2022-07-12", "1:30", "PM")
#print(time)

#print(pokedexInfo("r!poke Bulbasaur"))

import pyodbc 



#read(cnxn)
#create(cnxn)
#update(cnxn)
#delete(cnxn)

#cnxn.close()


def databaseRead():
    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                        "Server=DESKTOP-SQR7QOT\SQLEXPRESS;"
                        "Database=Cooking;"
                        "Trusted_Connection=yes")
    hello = ""
    print("read")
    cursor = cnxn.cursor()
    cursor.execute('select * from Recipes')
    for row in cursor:
        print (f'row = {row}')
        print (row[1])
        hello = hello + row[1]
    print(hello)
    return hello

print(databaseRead())
