from datetime import date

def getCurrentDate():
    currentDate = str(date.today())
    todayArr = currentDate.split("-")
    today = todayArr[1] + "/" + todayArr[2] + "/" + todayArr[0]
    return today