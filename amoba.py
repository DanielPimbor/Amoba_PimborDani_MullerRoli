
mezo = [
    ['_', '_','_',],
    ['_', '_', '_',],
    ['_', '_', '_',]
]

for sor in mezo:
    print(sor)

while True:
    hova_rakod_sor = int(input('Hanyadik sorba akarod rakni?'))
    hova_rakod_oszlop = int(input('Hanyadik oszlopba akarod rakni?'))

    if mezo[hova_rakod_sor - 1][hova_rakod_oszlop - 1] == '_':
        mezo[hova_rakod_sor - 1][hova_rakod_oszlop - 1] = 'X'
    else:
        print('Ide nem rakhatod.')

    for sor in mezo:
        print(sor)

