
print('Ez a program kiszámolja az átlagodat.')
print('Ha már nem akarsz több jegyet megadni, írj 0-át!')
print('--------------------------------------------')

darab = 0
osszeg = 0

erdemjegy = int(input('Add meg az első érdemjegyet: '))
while erdemjegy != 0:
	darab = darab + 1
	osszeg = osszeg + erdemjegy
	erdemjegy = int(input('Add meg az következő érdemjegyet: '))
	
if darab != 0:
	      print('A jegyeid átlaga: ', osszeg / darab)
else:
	      print('Nem adtál meg egy jegyet sem!')
  
  
'''
 Az ELDÖNTÉS esetében azt vizsgáljuk,
hogy szerepel-e egy bizonyos tulajdonságú elem az adatsorban (itt a listában).
    
A program azt vizsgálja, hogy van-e hárommal osztható szám a listában.
    '''
lista = [2, 5, 4, 8, 9, 11, 10, 12]
    
talalat = False
index = 0
while index < len(lista) and not talalat:
    if lista[index] % 3 == 0:
        talalat = True
    index = index + 1
    
    if talalat:
        print('Van a listában hárommal osztható szám.')
    else:
        print('Nincs a listában hárommal osztható szám.')

        
    '''
    Az KERESÉS esetében azt vizsgáljuk, 
    hogy szerepel-e egy bizonyos tulajdonságú elem az adatsorban (itt a listában),
    és ha igen, hányadik helyen.

    A program azt vizsgálja, hogy szerepel-e a piros szín a listában, és ha igen, hányadik helyen.
    '''
    lista = ['kék', 'zöld', 'piros', 'fehér']

    talalat = False
    index = 0
    while index < len(lista) and not talalat:
	      if lista[index] == 'piros':
		        talalat = True
index = index + 1

if talalat:
	      print('Van a listában piros szín, az indexe: ', index-1)
else:
	      print('Nincs a listában piros szín.')


'''
    A KIVÁLASZTÁS esetében azt tudjuk, hogy szerepel (legalább) egy bizonyos tulajdonságú elem 
    az adatsorban (itt a listában), és ennek az elemnek az indexére vagyunk kíváncsiak.

    A program azt vizsgálja, hogy hányadik indexű helyen áll a hárommal osztható szám a listában. 
    Az első ilyen elem előfordulása érdekel bennünket.  
    '''
lista = [2, 5, 4, 8, 9, 11, 10, 12]

talalat = False
index = 0
while not talalat:
	      if lista[index] % 3 == 0:
		        talalat = True
index = index + 1

print('A hárommal osztható szám indexe a listában: ', index-1)
    
    
'''
    A SZÁMLÁLÁS esetében azt vizsgáljuk, hogy egy bizonyos tulajdonságú elemből 
    hány darab van az adatsorban (itt a listában).

    A program azt vizsgálja, hogy hány darab hárommal osztható szám van a listában.
    '''
lista = [12, 5, 4, 8, 9, 11, 10, 12, 6]

darab = 0
for szam in lista:
	      if szam % 3 == 0:
		        darab = darab + 1

print('A listában lévő hárommal osztható számok száma: ', darab)  
  
  
'''
    A SZÉLSŐÉRTÉK MEGHATÁROZÁSA esetében azt vizsgáljuk, hogy melyik a legkisebb, 
    illetve a legnagyobb érték az adatsorban (itt a listában).
    '''
lista = [12, 5, 4, 8, 9, 11, 10, 12, 6]

min = lista[0]
max = lista[0]
for szam in lista:
	      if szam < min:
		        min = szam
if szam > max:
		        max = szam
print('A legkisebb szám a listában: ', min)
print('A legnagyobb szám a listában: ', max)  
  
  
  