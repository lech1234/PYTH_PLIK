"""
Moduł prezentuje instrukcje importu o postaci:
from <pakiet>.<podpakiet> import <modul>

Moduł tworzy listę instancji typu Osoba (dostępną globalnie)
"""
from sekcja01.model import adres as adr, osoba

osoby = [
    osoba.Osoba('Jan', 'Kowalski',
                adr.Adres('ul. Nadmorska 11', '12-345', 'Gdańsk')),
    osoba.Osoba('Adam', 'Bednarek',
                adr.Adres('ul. Polna 3', '23-456', 'Mrągowo')),
    osoba.Osoba('Anna', 'Jabłońska',
                adr.Adres('ul. Polska 42', '34-567', 'Kołobrzeg'))
]

if __name__ == '__main__':
    print('OSOBY:')
    # Do konwersji instancji na tekst używana jest standardowo funkcja str()
    print(*osoby, sep='\n')

    # Uwaga:
    # Przy konwersji listy na tekst, elementy listy są standardowo konwertowane na tekst za pomocą funkcji repr()
    print(osoby)
