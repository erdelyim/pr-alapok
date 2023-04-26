"""
# sorok vannak közötte 

forrasfajl = open("szoveg.txt")

for sor in forrasfajl:
    print(sor)
forrasfajl.close()

print("--------------------")

#nincsnnek sorok közötte

forrasfajl = open("szoveg.txt")

for sor in forrasfajl:
    print(sor, end='')
forrasfajl.close()

print("--------------------")


forrasfajl = open("szoveg.txt")

#egymás mellé rakja a szövegeket

for sor in forrasfajl:
    sor = sor.strip()
    print(sor, end='')
forrasfajl.close()

print("--------------------")

"""
with open("szoveg.txt", "r", encoding="UTF-8") as forrasfajl:
    for sor in forrasfajl:
        sor = sor.strip()
        print(sor)
