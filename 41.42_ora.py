lista = [2, 5, 4, 8, 19, 11, 10, 12]

talalat = False
index = 0
while not talalat:
    if lista[index] % 3 == 0:
        talalat = True
    index = index + 1 

print('A hárommal osztható szám indexe a listában: ', index-1)