"""
Moduł testujący działanie serializacji i deserializacji.
"""
if __name__ == '__main__':
    from serializacja import *
    from deserializacja import *

    # utworzenie listy osób (danych testowych)
    osoby = [
        ['Jan', 'Kowalski', True, 1990],
        ['Anna', 'Nowakowska', False, 2000]
    ]

    print('DANE PRZED SERIALIZACJĄ:')
    print(*osoby, sep='\n', end='\n\n')

    # zapis danych osób w formie strukturalnej do pliku binarnego
    print('SERIALIZACJA WSZYSTKICH OSÓB')
    serializuj(osoby, 'osoby.dat')

    # odczyt wszystkich osób z pliku binarnego
    print('\nDESERIALIZACJA WSZYSTKICH OSÓB')
    osoby = deserializuj_wszystkie_osoby('osoby.dat')
    print('\nDANE PO DESERIALIZACJI:')
    print(*osoby, sep='\n', end='\n\n')

    # odczyt danych osoby ze strukturalnego pliku binarnego na podstawie nr rekordu
    print('DESERIALIZACJA OSOBY #2:')
    osoba = deserializuj_osobe('osoby.dat', 1)  # numeracja rekordów zaczyna się od zera
    print(osoba)
