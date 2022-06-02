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
    end[1] = endTime[0] + ":" + endTime[1] + ":" + endTime[2]

    print(start)
    print(end)

    start_date = datetime.strptime(start[0], "%Y-%m-%d")
    end_date = datetime.strptime(end[0], "%Y-%m-%d")
    delta = relativedelta.relativedelta(end_date, start_date)

    start_time = datetime.strptime(start[1],"%H:%M:%S")
    end_time = datetime.strptime(end[1],"%H:%M:%S")

    time_interval = str(end_time - start_time) 
    timeDiff = time_interval.split(",")
    
    if delta.years == 0 and delta.months == 0 and delta.days == 0:
        if time_interval.startswith("-1 day"):
            return "Invalid End"
        else: 
            return time_interval
    elif delta.years == 0 and delta.months == 0 and delta.days == 1 and len(timeDiff)>1:
        return timeDiff[1]
    else:
        if delta.years == 0 and delta.months == 0 and delta.days == 0 and len(timeDiff) == 2:
            return "Invalid End"
        elif delta.years == 0 and delta.months == 0 and delta.days<4 and len(timeDiff) == 2:
            return str(delta.days -1) + " days " + timeDiff[1] + " chicken"
        elif delta.years == 0 and delta.months == 0 and len(timeDiff) == 2:
            return str(delta.days -1) + " days  pig" 
        elif delta.years == 0 and delta.months == 0:
            return str(delta.days) + " days "
        elif delta.years == 0:
            return str(delta.months) + " months, " + str(delta.days) + " days"
        else: 
            return str(delta.years) + " years, " + str(delta.months) + " months, " + str(delta.days) + " days"