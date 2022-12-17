import sys

# rozwiązanie mało eleganckie,
# ale potrzebujemy pełnych ścieżek do dystrybucji
base  = '\\'.join(__file__.split('\\')[:-3])  # ścieżka projektu
sys.path += [base + '\\distributions\\dist1', base + '\\distributions\\dist2']

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
