"""
szam = int(input("5-10 kozott"))
while not 5 <= szam <= 10:
    szam = int(input("Helytelen érték, mégegyszer"))

print("rendben")
"""
szo = None 
szoveg = ""
while szo != '':
    szo = input('Adj meg szavakat! Ha kilépnél, a szó helyet csak egy ENTER-t üss! ')
    print(szo+szoveg)
print('Program vége!')