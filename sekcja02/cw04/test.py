"""
Moduł testujący działanie serializacji i deserializacji.
"""
if __name__ == '__main__':
    from sekcja01.cw01.import1 import osoby

    from serializacja import *
    from deserializacja import *

    # plik danych
    sciezka_do_pliku = 'osoby.txt'

    print('DANE PRZED SERIALIZACJĄ:')
    print(*osoby, sep='\n', end='\n\n')

    serializuj(sciezka_do_pliku, osoby)
    lista_osob = deserializuj(sciezka_do_pliku)

    print('\nDANE ZDESERIALIZOWANE:')
    print(*lista_osob, sep='\n', end='\n\n')

    print('CZY RÓWNE?', osoby[0] == lista_osob[0])