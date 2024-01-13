"""
Moduł prezentuje instrukcje importu o postaci:
from <pakiet>.<podpakiet> import *

Moduł tworzy listę instancji typu Osoba (dostępną globalnie)
"""
from ...model import *

# Trzeba zdefiniować atrybut __all__ w pliku __init__.py, aby wskazać które moduły będą importowane.
# Zastosowano importy względne

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
    # Do konwersji instancji na tekst używana jest standardowo funkcja str()
    print(*osoby, sep='\n')

    # Uwaga:
    # Przy konwersji listy na tekst, elementy listy są standardowo konwertowane na tekst za pomocą funkcji repr()
    print(osoby)
