# 1.1 
"""
print('Nagybetűsen:', input('Szó: ').upper())

"""
# 1.2

"""
lista = ['nem', 'kell', 'nekem', 'semmilyen', 'egyes', 'jegyek', 'minden', 'jó', 'lesz']

mas_lista = [szo.upper() for szo in lista]

print('Eredeti:', lista)
print('Nagybetűs:', mas_lista)

"""
# 1.3

"""
lista = ['nem', 'kell', 'nekem', 'semmilyen', 'egyes', 'jegyek', 'minden', 'jó', 'lesz']

mas_lista = [szo.upper() for szo in lista if len(szo) > 3]

print('Eredeti:', lista)
print('Nagybetűs:', mas_lista)
"""
# 1.4
'''
lista = ['padlo', 'macska', 'ember']

mas_lista = [szo.swapcase() for szo in lista]

print('Eredeti:', lista)
print('Ellentétesbetűs:', mas_lista)
'''
# 2.1

"""
ertelmezesi_tartomany = list(range(-3, 5))

ertek_keszlet = [2 * x - 3 for x in ertelmezesi_tartomany]

print('Értelemzési tartomány:', ertelmezesi_tartomany)
print('Érték készlet:', ertek_keszlet)
"""
#2.2
"""
ertelmezesi_tartomany = list(range(-3, 5))

ertek_keszlet = [2 * x - 3 for x in ertelmezesi_tartomany if x >= 0]

print('Értelemzési tartomány:', ertelmezesi_tartomany)
print('Érték készlet:', ertek_keszlet)
"""
#1.1

paletta = ['kék', 'piros', 'fehér', 'fekete', 'zöld', 'sárga', 'barna', 'piros', 'fehér', 'szürke']

szin = input('Adj meg egy színt!\t')
if szin in paletta:
	print('A megadott szín szerepel a listában.')
else:
	print('A megadott szín nem szerepel a listában.')

print('A lista színei:')
for szin in paletta:
	print(szin, end=', ')
#1.2

