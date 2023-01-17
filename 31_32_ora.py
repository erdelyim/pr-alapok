"""
nev = input("kereszt nev: ")
kor = int(input("hany eves vagy: "))

if kor < 1:
    print("A kora alapján" , nev, "csecsemő")

elif kor < 6:
    print("A kora alapján" , nev, "kisgyerek")

elif kor < 12:
    print("A kora alapján" , nev, "gyerek")

elif kor < 16:
    print("A kora alapján" , nev, "serdülő")

elif kor < 25:
    print("A kora alapján" , nev, "ifjú")

elif kor < 65:
    print("A kora alapján" , nev, "felnőtt")

else:
    print("A kora alapján" , nev, "nyugdíjas")
"""

t = [7, 8, 6, 2, 15, 1, 13, 5, 9, 11, 12, 3, 4]
print(t)
lista_hossza=len(t)
print(f"A lista hossza: {lista_hossza}")
for i  in range(lista_hossza-1, 0, -1):
    for j in range(0, i):
        if t[j] > t[j+1]:
            tmp= t[j+1]
            t[j]= tmp
            print(f"(t) i = {i} j = {j}")
