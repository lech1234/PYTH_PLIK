"""
Moduł prezentuje instrukcje importu o postaci:
from <pakiet>.<podpakiet>.<modul> import <atrybut>

Moduł tworzy listę instancji typu Osoba (dostępną globalnie)
"""
from sekcja01.model.osoba import Osoba
from sekcja01.model.adres import *

osoby = [
    Osoba('Jan', 'Kowalski',
          Adres('ul. Nadmorska 11', '12-345', 'Gdańsk')),
    Osoba('Adam', 'Bednarek',
          Adres('ul. Polna 3', '23-456', 'Mrągowo')),
    Osoba('Anna', 'Jabłońska',
          Adres('ul. Polska 42', '34-567', 'Kołobrzeg'))
]

if __name__ == '__main__':
    print('OSOBY:')
    # Do konwersji instancji na tekst używana jest standardowo funkcja str()
    print(*osoby, sep='\n')

    # Uwaga:
    # Przy konwersji listy na tekst, elementy listy są standardowo konwertowane na tekst za pomocą funkcji repr()
    print(osoby)
