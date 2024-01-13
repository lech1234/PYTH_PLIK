"""
MOduł prezentuje użycie pakietów przestrzeni nazw.
"""
import sys

# Rozwiązanie mało eleganckie, ale potrzebujemy pełnych ścieżek do dystrybucji

# Atrybut __file__ modułu reprezentuje pełną ścieżkę do bieżącego modułu.
# Z tej ścieżki usuwamy końcówkę z nazwami pakietów, aby pozostawić ścieżkę do projektu
sciezka_projektu = '\\'.join(__file__.split('\\')[:-3])

# Do atrybutu sys.path dodajemy ścieżki do dystrybucji
# Dystrybucje nie posiadają plików __init__.py
sys.path += [
    sciezka_projektu + '\\dystrybucje\\dystr_a',
    sciezka_projektu + '\\dystrybucje\\dystr_b'
]

# Poniższe błędy (unresolved reference) trzeba zignorować
# W momencie uruchomienia modułu powinno być dobrze, gdyż zmienna sys.path została zaktualizowana
# programowo (dynamicznie)
from model import osoba, adres

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
