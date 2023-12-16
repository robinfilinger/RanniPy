import pandas as pd
from Functions.countdowns import addCountdown, isCountdownValid, isCountdownTitle, timeUntil, getTotalCountdowns, getAllCountdowns, printAllCountdowns, getCountdown
import re
from Functions.dates import holidayList
from Functions.misc import toTable

from Functions.pets import getPet, getTotalPets, getAllPets
from Functions.pokemon import pokedexInfo

#args = ["command", "Together", "07/02/10", "9:30", "PM"]
#print(addCountdown(args)

#time = timeUntil("2022-07-12", "1:30", "PM")
#print(time)

#print(pokedexInfo("r!poke Bulbasaur"))

import pyodbc 
from datetime import date, datetime
import holidays

# Select country
#us_holidays = holidays.US()
#print(us_holidays)
#print(us_holidays.get('2022'))

# Print all the holidays in US in year 2018
#for hol in holidays.US(years = 2022).items():
#    print(hol)

#print(holidays.US(years = 2022).items())
#calendar = holidays.US(years = 2022).items()
#for x in calendar:
    #print(str(x))


#print(getAllCountdowns())


#print(isCountdownTitle('r!addCountdown “RANNI REUNITES” 2022-12-29 10:00 AM'))
# print('------------------------------------------')
# print(addCountdown('r!addCountdown "Ranni January :)" 2023-01-26 07:00 PM'))

print(holidayList())











#read(cnxn)
#create(cnxn)
#update(cnxn)
#delete(cnxn)

#cnxn.close()


#def databaseRead():
    #cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                        #"Server=DESKTOP-SQR7QOT\SQLEXPRESS;"
                        #"Database=Cooking;"
                        #"Trusted_Connection=yes")
    #hello = ""
    #print("read")
    #cursor = cnxn.cursor()
    #cursor.execute('select * from Recipes')
    #for row in cursor:
    #    print (f'row = {row}')
    #    print (row[1])
    #    hello = hello + row[1]
    #print(hello)
    #return hello

#print(databaseRead())
