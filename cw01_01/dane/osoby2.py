# from pakiet.podpakiet import modul
from cw01_01.model import osoba, adres as a

osoby = [
    osoba.Osoba('Jan', 'Kowalski',
                a.Adres('ul. Nadmorska 11', '12-345', 'Gdańsk')),
    osoba.Osoba('Adam', 'Bednarek',
                a.Adres('ul. Polna 3', '23-456', 'Mrągowo')),
    osoba.Osoba('Anna', 'Jabłońska',
                a.Adres('ul. Polska 42', '34-567', 'Kołobrzeg'))
]

if __name__ == '__main__':
    print('OSOBY:')
    print(*osoby, sep='\n')
