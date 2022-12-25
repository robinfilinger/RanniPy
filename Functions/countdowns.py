from datetime import date, datetime
from time import time
from dateutil import relativedelta
import pandas as pd
from Functions.dates import MDYtoDMY, getCurrentDate, printYMD
from Functions.length import dateDiff
from table2ascii import table2ascii as t2a, PresetStyle
import re

countdownTitle = ""
countdownInfo = ""

#adds countdown
def addCountdown(message):
    if isCountdownValid(message):
        countdownInfo = replaceTitle(message)
        args = countdownInfo.split(" ")

        df = pd.read_csv('Data/SaveFiles/countdowns.csv')
        df.loc[len(df.index)] = [getCountdownTitle(message), args[2], args[3], args[4]]
        df.to_csv('Data/SaveFiles/countdowns.csv', index=False)
        return "Countdown *" + getCountdownTitle(message) + "* has been added!"
    else:
        return countdownError()

#checks that countdown is properly formatted
def isCountdownValid(message):
    if isCountdownTitle(message) == False:
        return False

    countdownInfo = replaceTitle(message)
    print(countdownInfo)
    args = countdownInfo.split(" ")
    print(countdownInfo)

    if len(args) != 5:
        print("length false")
        return False
    if bool(re.match("[2][0-9][0-9][0-9]-[0-1][0-9]-[0-3][0-9]", args[2])) == False:
        print("date false")
        return False
    if bool(re.match("[0-1][0-9]:[0-5][0-9]", args[3])) == False:
        print("time false")
        return False
    if args[4] != "AM" and args[4] != "PM":
        print("Meridem false")
        return False
    return True

#checks to see if there is a string surrounded by quotes
def isCountdownTitle(message):
    counter = message.count('"') + message.count('“') + message.count('”')
    print(counter)
    if counter == 2: 
        if len(getCountdownTitle(message))>0:  
            print("Countdown Title exists")
            return True
    return False

#returns title between two quotes
def getCountdownTitle(message):
    if '"' in message:
        title = re.search('"(.*)"', message)
    else:
        title = re.search('“(.*)”', message)
    return title.group(1) 

#replaces title with placeholder
def replaceTitle(message):
    if '"' in message:
        return re.sub('".*?"', 'title', message)
    else:
        return re.sub('“.*?”', 'title', message)
    

#returns error message with proper formatting instructions
def countdownError():
    return '**Please enter countdown and end date in the following format:**\n\nr!addCountdown **"Countdown Name"** YYYY-MM-DD HH:MM AM/PM\n\nExample: r!addCountdown "Reunited" 2023-12-21 12:30 PM' 

def getTotalCountdowns():
    df = pd.read_csv('Data/SaveFiles/countdowns.csv')
    return len(df.index)

def getCountdown(index):
    df = pd.read_csv('Data/SaveFiles/countdowns.csv')
    countdown = [df.iloc[index]["Name"],
        timeUntil(df.iloc[index]["End Date"], df.iloc[index]["End Time"], df.iloc[index]["Meridem"] ),
        ]
    return [countdown]

def getAllCountdowns():
    countdownArray = []
    for i in range(getTotalCountdowns()):
        countdown = getCountdown(i)
        countdownArray = countdownArray + countdown
        #countdownArray = countdownSort(countdownArray)
    return countdownArray

def countdownSort(countdowns):
    df = pd.DataFrame(columns=['Id', 'Name', 'End Date', 'End Time', 'Meridem'])
    for x in countdowns:
        if timeUntil(df.iloc[x]["End Date"], df.iloc[x]["End Time"], df.iloc[x]["Meridem"]) > 0:
            df.concat()


def printAllCountdowns():
    output = t2a(
    header=["Title", "Time Remaining"],
    body=getAllCountdowns(),
    )
    return output


#takes an end date and time and calculates time until that date and time
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

    start_date = datetime.strptime(start[0], "%Y-%m-%d")
    end_date = datetime.strptime(end[0], "%Y-%m-%d")
    delta = relativedelta.relativedelta(end_date, start_date)


    if(delta.days<=3):
        start_time = datetime.strptime(start[1],"%H:%M:%S")
        end_time = datetime.strptime(end[1],"%H:%M:%S")
        return str(delta.days) 
    else:
        return printYMD(delta.years, delta.months, delta.days)

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
            return str(delta.days -1) + " days " + timeDiff[1]
        elif delta.years == 0 and delta.months == 0 and delta.days<4 and len(timeDiff) == 1:
            return str(delta.days) + " days " + time_interval
        elif delta.years == 0 and delta.months == 0 and len(timeDiff) == 2:
            return str(delta.days -1) + " days" 
        elif delta.years == 0 and delta.months == 0:
            return str(delta.days) + " days "
        elif delta.years == 0:
            return str(delta.months) + " months, " + str(delta.days) + " days"
        else: 
            return str(delta.years) + " years, " + str(delta.months) + " months, " + str(delta.days) + " days"