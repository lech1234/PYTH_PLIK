"""
Moduł prezentuje instrukcje importu o postaci:
import <pakiet>.<podpakiet>.<modul>

Tu muszą pozostać importy bezwzględne.
Importy względne funkcjonują tylko dla importów typu: from ... import ...
"""
import sekcja01.model.osoba
import sekcja01.model.adres as adr

osoby = [
    sekcja01.model.osoba.Osoba('Jan', 'Kowalski',
                               adr.Adres('ul. Morska 11', '12-345', 'Gdańsk')),
    sekcja01.model.osoba.Osoba('Adam', 'Bednarek',
                               adr.Adres('ul. Polna 3', '23-456', 'Mrągowo')),
    sekcja01.model.osoba.Osoba('Anna', 'Jabłońska',
                               adr.Adres('ul. Polska 42', '34-567', 'Kołobrzeg'))
]

if __name__ == '__main__':
    print('OSOBY:')
    # Do konwersji instancji na tekst używana jest standardowo funkcja str()
    print(*osoby, sep='\n')

    # Uwaga:
    # Przy konwersji listy na tekst, elementy listy są standardowo konwertowane na tekst za pomocą funkcji repr()
    print()
    print(osoby)
