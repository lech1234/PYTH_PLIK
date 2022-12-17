# from pakiet.podpakiet.modul import atrybut
from ..model.osoba import Osoba
from ..model.adres import *

osoby = [
    Osoba('Jan', 'Kowalski',
          Adres('ul. Morska 11', '12-345', 'Gdańsk')),
    Osoba('Adam', 'Bednarek',
          Adres('ul. Polna 3', '23-456', 'Mrągowo')),
    Osoba('Anna', 'Jabłońska',
          Adres('ul. Polska 42', '34-567', 'Kołobrzeg'))
]

if __name__ == '__main__':
    print('OSOBY:')
    print(*osoby, sep='\n')
