# Eljárás paraméterel:

nev1 = "10.C"  # ez a globális változó 
def koszont_nevvel(nev):
    print('Szia '+ nev +', üdv a fedélzeten!')
    print(f"Szia {nev}, üdv a fedélzeten!")
    print(f"Szia {nev}, üdv a fedélzeten!")

koszont_nevvel('Ádám') # Ádám - aktualis paraméter




# Eljárás 2 paramétere:

def koszont_ket_nevvel(nev1, nev2):
    print(f"szia {nev1} {nev2} udv a fedélzeten")

koszont_ket_nevvel("béla", "jani")
