from datetime import datetime, date
from dateutil import relativedelta

def length():
    start = '10/1/2022'

    #get today's date in dd/mm/yyyy
    today = str(date.today())
    todayArr = today.split("-")
    today = todayArr[2] + "/" + todayArr[1] + "/" + todayArr[0]

    # convert string to date object
    start_date = datetime.strptime(start, "%d/%m/%Y")
    end_date = datetime.strptime(today, "%d/%m/%Y")

    # Get the relativedelta between two dates
    delta = relativedelta.relativedelta(end_date, start_date)

    if delta.years == 0 and delta.months == 0:
        length = '🥰Ranni has been together for ' + str(delta.days) + ' days!🥰'
    elif delta.years == 0 and delta.days == 0:
        length = '🥰Ranni has been together for ' + str(delta.months) + ' months!🥰'
    elif delta.months == 0 and delta.days == 0:
        length = '🥰Ranni has been together for ' + str(delta.years) + ' years! Happy Anniversary!🥰'
    elif delta.years == 0:
        length = '🥰Ranni has been together for ' + str(delta.months) + ' months, and ' + str(delta.days) + ' days!🥰'
    elif delta.months == 0:
        length = '🥰Ranni has been together for ' + str(delta.years) + ' years, and ' + str(delta.days) + ' days!🥰'
    elif delta.days == 0:
        length = '🥰Ranni has been together for ' + str(delta.years) + ' years, and ' + str(delta.months) + ' months!🥰'
    else: 
        length = '🥰Ranni has been together for ' + str(delta.years) + ' years, ' + str(delta.months) + ' months, and ' + str(delta.days) + ' days!🥰'
    return length

def dateDiff(start, end):
    start_date = datetime.strptime(start, "%d/%m/%Y")
    end_date = datetime.strptime(end, "%d/%m/%Y")

    delta = relativedelta.relativedelta(end_date, start_date)

    return str(delta.years) + " years, " + str(delta.months) + " months, and " + str(delta.days) + " days" 

