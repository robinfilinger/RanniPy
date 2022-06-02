import pandas as pd
from Functions.countdowns import addCountdown, timeUntil

from Functions.pets import getPet, getTotalPets

args = ["command", "Together", "5/5/10", "9:30", "PM"]
#print(addCountdown(args))

time = timeUntil("2022-06-08", "2:30", "PM")
print(time)
