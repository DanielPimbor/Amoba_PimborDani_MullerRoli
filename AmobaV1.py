print('\n')
print('Köszöntelek a Python alapú amőba játékban!')
print('A cél, hogy 3 azonos jel egymás mellé kerüljön.\n')


def tabla_kiir(i):
    for sor in i:
        for adat in sor:
            print(adat, end=" ")
        print()

def nyeres(jel):
    return (
        # sorok
        (mezo[0][0] == jel and mezo[0][1] == jel and mezo[0][2] == jel) or
        (mezo[1][0] == jel and mezo[1][1] == jel and mezo[1][2] == jel) or
        (mezo[2][0] == jel and mezo[2][1] == jel and mezo[2][2] == jel) or

        # oszlopok
        (mezo[0][0] == jel and mezo[1][0] == jel and mezo[2][0] == jel) or
        (mezo[0][1] == jel and mezo[1][1] == jel and mezo[2][1] == jel) or
        (mezo[0][2] == jel and mezo[1][2] == jel and mezo[2][2] == jel) or

        # átlók
        (mezo[0][0] == jel and mezo[1][1] == jel and mezo[2][2] == jel) or
        (mezo[0][2] == jel and mezo[1][1] == jel and mezo[2][0] == jel)
    )


def döntetlen():
    for sor in mezo:
        if '_' in sor:
            return False
    return True


while True:

    mezo = [
        ['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_']
    ]

    tabla_kiir(mezo)

    while True:

        # 1. játékos
        print('\n1. játékos (X), te jössz.')

        while True:
            sor = int(input('Hanyadik sorba rakod? (1-3): '))
            oszlop = int(input('Hanyadik oszlopba rakod? (1-3): '))

            if sor < 1 or sor > 3 or oszlop < 1 or oszlop > 3:
                print('Hibás koordináta.')
                continue

            if mezo[sor - 1][oszlop - 1] != '_':
                print('Ide nem rakhatsz.')
                continue

            mezo[sor - 1][oszlop - 1] = 'X'
            break
        
        print('\n')
        tabla_kiir(mezo)

        if nyeres('X'):
            print('\nAz 1. játékos nyert!')
            break

        if döntetlen():
            print('\nDöntetlen!')
            break

        # 2. játékos
        print('\n2. játékos (O), te jössz.')

        while True:
            sor = int(input('Hanyadik sorba rakod? (1-3): '))
            oszlop = int(input('Hanyadik oszlopba rakod? (1-3): '))

            if sor < 1 or sor > 3 or oszlop < 1 or oszlop > 3:
                print('Hibás koordináta.')
                continue

            if mezo[sor - 1][oszlop - 1] != '_':
                print('Ide nem rakhatsz.')
                continue

            mezo[sor - 1][oszlop - 1] = 'O'
            break
        
        print('\n')
        tabla_kiir(mezo)

        if nyeres('O'):
            print('\nA 2. játékos nyert!')
            break

        if döntetlen():
            print('\nDöntetlen!')
            break

    ujra = input('\nAkartok még játszani? (i/n): ')

    if ujra != 'i':
        print('Viszláááát!')
        break