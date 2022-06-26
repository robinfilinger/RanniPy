from datetime import date, datetime
from dateutil import relativedelta
import pandas as pd
from Data.Arrays.petArrays import petEmojis, petNatures
from Functions.dates import MDYtoDMY, getCurrentDate, printYMD
from Functions.length import dateDiff
from table2ascii import table2ascii as t2a, PresetStyle
import re

countdownTitle = ""
countdownInfo = ""


def addCountdown(message):
     
    if isCountdownValid(message):
        return getCountdownTitle("true")

        #df = pd.read_excel('Data/SaveFiles/countdowns.xlsx')
        #df.loc[len(df.index)] = [args[1], args[2], args[3], args[4]]
        #print(df)
        #df.to_excel('Data/SaveFiles/countdowns.xlsx', index=False)
        #return "Countdown *" + args[1] + "* has been added!"
    return countdownError()

def isCountdownValid(message):
    if isCountdownTitle(message) == False:
        return False

    countdownTitle = getCountdownTitle(message)
    countdownInfo = replaceTitle(message)
    args = countdownInfo.split(" ")

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
    counter = message.count('"')
    if counter == 2: 
        if len(getCountdownTitle(message))>0:  
            return True
    return False

#returns title between two quotes
def getCountdownTitle(message):
    title = re.search('"(.*)"', message)
    return title.group(1)

#returns error message with proper formatting instructions
def countdownError():
    return 'Please enter countdown and end date in the following format:\n\nr!addCountdown **"Countdown Name"** YYYY-MM-DD HH:MM AM/PM\n\nExample: r!addCountdown "Reunited" 12:30 PM' 

def replaceTitle(message):
    return re.sub('".*?"', 'title', message)
    

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


    if(delta.days<=3):
        start_time = datetime.strptime(start[1],"%H:%M:%S")
        end_time = datetime.strptime(end[1],"%H:%M:%S")
        return 
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