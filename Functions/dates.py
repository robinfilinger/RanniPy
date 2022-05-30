from datetime import date

def getCurrentDate():
    currentDate = str(date.today())
    todayArr = currentDate.split("-")
    today = todayArr[1] + "/" + todayArr[2] + "/" + todayArr[0]
    return today

def MDYtoDMY(date):
    todayArr = date.split("/")
    return todayArr[1] + "/" + todayArr[0] + "/" + todayArr[2]
