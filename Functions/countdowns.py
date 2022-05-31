from datetime import date, datetime
from dateutil import relativedelta
import random
from tracemalloc import start
import pandas as pd
from Data.Arrays.petArrays import petEmojis, petNatures
from Functions.dates import MDYtoDMY, getCurrentDate
from Functions.length import dateDiff
from table2ascii import table2ascii as t2a, PresetStyle

def addCountdown(args):
    df = pd.read_excel('Data/SaveFiles/countdowns.xlsx')
    df.loc[len(df.index)] = [args[1], args[2], args[3], args[4]]
    print(df)
    df.to_excel('Data/SaveFiles/countdowns.xlsx', index=False)
    return "Countdown *" + args[1] + "* has been added!"

def timeUntil(endDate, endTime, Meridem):
    today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    start = str(today).split(" ")
    print(start)

    endList = endDate + " " + endTime + ":00"
    end = endList.split(" ")
    endTime = end[1].split(":")
    if Meridem == "AM":
        if int(endTime[0]) <10:
            endTime[0] = "0" + endTime[0]
        if int(endTime[0]) == 12:
            endTime[0] = "00"
    elif Meridem == "PM":
        if int(endTime[0]) !=12:
            endTime[0] = str(int(endTime[0]) + 12)

    print(end)
    print(endTime)
    #print(endList)
    
    #print(str(datetime.now()))
    #print(end)
    #endtime = datetime.strptime(end, "%Y-%m-%d %H:%M:%S")

    #start_date = datetime.strptime(today, "%d/%m/%Y")
    #end_date = datetime.strptime(end, "%d/%m/%Y")

    #delta = relativedelta.relativedelta(today, endTime)

    #print(str(today))
    #print(str(endtime))
    return
