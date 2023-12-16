from datetime import date
import holidays
import pandas as pd
from Data.Arrays.holidays import holidayInfo
from Functions.misc import toTable


def getCurrentDate():
    currentDate = str(date.today())
    todayArr = currentDate.split("-")
    today = todayArr[1] + "/" + todayArr[2] + "/" + todayArr[0]
    return today

def MDYtoDMY(date):
    todayArr = date.split("/")
    return todayArr[1] + "/" + todayArr[0] + "/" + todayArr[2]

def printYMD(years, months, days): 
    if years == 0 and months == 0:
        return str(days) + " days "
    elif years == 0:
        return str(months) + " months, " + str(days) + " days"
    else: 
        return str(years) + " years, " + str(months) + " months, " + str(days) + " days"

def isTodayHoliday():
    calendar = holidayList()
    
    #get today's holiday
    today = calendar.loc[calendar['Date'] == str(date.today())]
    todaylength = len(today)
    todayResult = today.values.tolist()

    if todaylength == 0:
        return 'No holidays today!'
    else:
        for x in range(len(holidayInfo)):
            if holidayInfo[x][0] == todayResult[0][1]:
                return holidayInfo[x][1]
    return 'No holidays today!'
       
def holidayList():
    #get current year
    year = date.today().year

    #get US and Mexico holiday list from this year
    holidaysUS = list(holidays.US(years = year, observed = False).items())
    holidaysMX = list(holidays.MX(years = year).items())

    calendar = pd.DataFrame(holidaysUS)
    #Mexico calendar does not look accurate
    #calendarMX = pd.DataFrame(holidaysMX)
    #calendar = pd.concat([calendarUS,calendarMX]).drop_duplicates().reset_index(drop=True)

    #rename columns to name and date
    calendar.rename(columns={calendar.columns[0]: 'Date', calendar.columns[1]: 'Name'},inplace=True)
    
    #Add *Special holidays
    moreHolidays = pd.DataFrame({'Date': [str(year)+'-01-10',str(year)+'-07-27',str(year)+'-08-25',str(year)+'-11-01',str(year)+'-11-02',str(year)+'-12-24'],
                                 'Name': ['Ranni Day', 'Danni Day', 'Riccardo Day', 'Dia de Los Muertos', 'Dia de Los Muertos', 'Christmas Eve']})
    calendar = pd.concat([calendar,moreHolidays]).reset_index(drop=True)
    calendar['Date'] = calendar['Date'].astype(str)

    #columns = calendar.columns.values
    columns = []
    for col in calendar.columns:
        columns.append(col)
    holidaysList = calendar.values.tolist() 
    
    return toTable(columns,holidaysList)

   