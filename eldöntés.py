# van egy nagy elemű lista sorozat, a sosrozatban van egy nagy T tulajdonság és az algoritmusom, 
# meg adja nekem hogy van e a sorozatban ilyen T tulajdonságú elem. (IGEN/NEM)

lista = [2, 5, 4, 8, 19, 11, 10, 13]

találat = False
index = 0 
while index < len(lista) and not találat:
    if lista[index] % 3 == 0:
        találat = True
    index = index + 1


if találat:
    print('Van a listában hárommal osztható szám.')
else: 
    print('Nincs a listában hárommmal osztható szám.')

print(találat)
