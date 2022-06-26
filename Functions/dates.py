from datetime import date

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