#feladat 1
"""
szam1 = int(input("kérek egy egész számot:"))
szam2 = int(input("kérek egy másik egész számot:"))
if szam1 > szam2:
    print("szam1 nagyobb mint szam2")
if szam2 > szam1:
    print("szam2 nagyobb mint szam1")
if szam1 == szam2:
    print("szam1 megyegyezik a szam2-vel") 
"""
#---------------------------------------------------
"""
szam1 = int(input("kérek egy egész számot:"))
szam2 = int(input("kérek egy másik egész számot:"))
if szam1 > szam2:
    print("szam1 nagyobb mint szam2")
elif szam2 > szam1:
    print("szam2 nagyobb mint szam1")
elif szam1 == szam2:
    print("szam1 megyegyezik a szam2-vel") 
"""
#----------------------------------------------------
"""
szam1 = int(input("kérek egy egész számot:"))
szam2 = int(input("kérek egy másik egész számot:"))
if szam1 > szam2:
    print("szam1 nagyobb mint szam2")
elif szam2 > szam1:
    print("szam2 nagyobb mint szam1")
else:
    print("szam1 megyegyezik a szam2-vel") 
"""
#-----------------------------------------------------
"""
from pickle import NONE
from re import X


x = None
print(x)
print(type(x))

if x:
    print("Do you think None is True?")
elif x is False:
    print("Do you think None is False?")
else: 
    print("None is not True, or False, None is just None...")
"""
#-------------------------------------------------------