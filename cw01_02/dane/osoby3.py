# from pakiet.podpakiet import *
from ..model import *

# trzeba zdefiniować atrybut __all__ w pliku setup.py, aby wskazać które moduły
# będą importowane

osoby = [
    osoba.Osoba('Jan', 'Kowalski',
                adres.Adres('ul. Morska 11', '12-345', 'Gdańsk')),
    osoba.Osoba('Adam', 'Bednarek',
                adres.Adres('ul. Polna 3', '23-456', 'Mrągowo')),
    osoba.Osoba('Anna', 'Jabłońska',
                adres.Adres('ul. Polska 42', '34-567', 'Kołobrzeg'))
]

if __name__ == '__main__':
    print('OSOBY:')
    print(*osoby, sep='\n')
