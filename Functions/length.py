from datetime import datetime, date
from dateutil import relativedelta

def dateDiff(start, end):
    start_date = datetime.strptime(start, "%d/%m/%Y")
    end_date = datetime.strptime(end, "%d/%m/%Y")

    delta = relativedelta.relativedelta(end_date, start_date)

    deltas = [delta.years, delta.months, delta.days]
    timeUnits = ['year', 'month', 'day']
    FinalDeltas = []

    for i in range(3):
        if deltas[i] == 1:
            FinalDeltas.append(str(deltas[i]) + ' ' + timeUnits[i])
        elif deltas[i] != 0:
            FinalDeltas.append(str(deltas[i]) + ' ' + timeUnits[i] + 's')

    lengthStart = '🥰Ranni has been together for '
    lengthEnd = '!🥰'
    if len(FinalDeltas) == 1:
        lengthMiddle = FinalDeltas[0]
    elif len(FinalDeltas) == 2:
        lengthMiddle = FinalDeltas[0] + ', and ' + FinalDeltas[1]
    else:
        lengthMiddle = FinalDeltas[0] + ', ' + FinalDeltas[1] + ', and ' + FinalDeltas[2]

    

    return lengthStart + lengthMiddle + lengthEnd

def formatToday():
    today = str(date.today())
    todayArr = today.split("-")
    today = todayArr[2] + "/" + todayArr[1] + "/" + todayArr[0]
    return today


