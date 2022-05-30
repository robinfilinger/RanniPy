import pandas as pd

from Functions.pets import getPet, getTotalPets


TwoD = []
TwoD = TwoD + [[2,30,40,35,40]]
pet = [[1,2,3,4,5,]]
TwoD = TwoD + pet
print(TwoD)

petArray = []

for i in range(getTotalPets()):
    print(i)
    pet = getPet(i)
    print(pet)
    petArray = petArray + pet

print(petArray)