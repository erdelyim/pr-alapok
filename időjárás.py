# március 22-től számoljuk a szünetig április 6.-ig
# Hány darab min és max van a listában 

napi_maximum = [14, 17, 21, 15, 16, 13, 8, 11, 12, 14, 16, 16, 14, 15, 13, 14, 16, 16, 14, 12, 12, 10, 11, 13, 15, 17, 19, 17, 19, 20]
napi_minimum = [8, 8, 9, 6, 7, 1, 0, 2, 3, 5, 4, 4, 3, 5, 4, 6, 8, 6, 4, 2, 1, -1, -1, 1, 3, 5, 7, 5, 7, 9, ]

napi_minimum_darab = None
napi_maximum_darab = None

def napi_maxmimum_fv():
    darab = 0 
    for szam in napi_maximum:
        darab += 1
        napi_maximum_darab = darab
        print(darab)
    napi_maxmimum_fv()

def napi_minimum_fv():
    darab = 0 
    for szam in napi_minimum:
        darab += 1
        napi_minimum_darab = darab
        print(darab)
    napi_minimum_fv()

def atlag_max(napi_max):
    darab = 0 
    for szam in napi_max:
        darab = darab = szam 
        atlag = darab / len(napi_max)
        print(darab)
    atlag_max()

def atlag_min(napi_min):
    darab = 0 
    for szam in napi_min:
        darab = darab = szam 
        atlag = darab / len(napi_min)
        print(darab)
    atlag_min()