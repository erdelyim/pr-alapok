# Bekérek egy osztályzatot, írja ki 1-elégtelen..5-jeles..vagy nem érvényes osztályzatot!
"""
jegy = input("kérek egy osztályzatot:")
if jegy == "1":
    print("elégtelen")
elif jegy == "2":
    print("elégséges")
elif jegy == "3":
    print("közepes")
elif jegy == "4":
    print("jó")
elif jegy == "5":
    print("jeles")
else: 
    print("Nem érvényes osztályzat")
"""
#-----------------------------------------------------------

# Bekérek egy pozitív egész számot, írja ki hogy páros vagy páratlan
"""
szam = int(input("kérek egy pozitív egész számot"))

if szam % 2 == 0:
    print("a szam páros")
else: 
    print("a szam páratlan")
"""
#-----------------------------------------------------------

# Random szám előállítás...
"""
import random

gondolt_szam = random.randint(1,6)
print('Súgok:', gondolt_szam)
tipp = input('Gondoltam egy számra. Tippeld meg! ')

"""
#-----------------------------------------------------------

# generáljunk egy számot 1-1000 között, írja ki a számot, ha páros és kisebb mint 500, ha ez nem igaz akkor 

import random 

szam = random.randint(1,1000)

print(szam)
if szam <= 500 and szam % 2 == 1:
    print("Patikaaa")
else:
    print("a szam nem felel meg")
