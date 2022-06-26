import pandas as pd
from Functions.countdowns import addCountdown, isCountdownValid, timeUntil
import re

from Functions.pets import getPet, getTotalPets

#args = ["command", "Together", "07/02/10", "9:30", "PM"]
#print(addCountdown(args)
print(addCountdown('r!addCountdown "hi there"'))

time = timeUntil("2022-06-08", "1:30", "PM")
print(time)

s = "2020-11-11"
t = re.sub('".*?"', 'title', s)
print(bool(re.match("[2][0-9][0-9][0-9]-[0-1][0-9]-[0-3][0-9]", s)))

print("testing isCountdownValid")
tester = 'r!addCountdown "title" 2022-12-25 12:30 PM'.split(" ")
print(tester)

print(isCountdownValid('r!addCountdown hello 2022-12-25 12:30 PM'))
print(isCountdownValid('r!addCountdown "hi there" 2022-12-25 12:30 AM'))

print(isCountdownValid('r!addCountdown "hi there" 2022-12-25 12:30 pen'))
print(isCountdownValid('r!addCountdown "hi there 2022-12-25 12:30 PM hello'))



