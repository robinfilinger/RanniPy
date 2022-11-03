from datetime import date
import holidays
import pandas as pd


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

def holidayList():
    year = date.today().year
    calendar = list(holidays.US(years = year).items())
    df = pd.DataFrame(calendar)
    df.rename(columns={df.columns[0]: 'Date', df.columns[1]: 'Name'},inplace=True)
    print(df.columns)
    print(df['Date'])
    print(df)
    print(date.today())
    return calendar[1]
     