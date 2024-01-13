"""
Moduł zawiera funkcje umożliwiające serializację sekwencji osób do strukturalnego pliku binarnego.

Zakładamy, że osobę opisuje lista zawierająca:
- imię (o długości nie większej niż 20 znaków)
- nazwisko (o długości nie większej niż 20 znaków)
- płeć (wartość logiczna)
- rok urodzenia (liczba całkowita)
"""
import struct


def __spakuj_do_struktury(osoba):
    """
    Funkcja pomocnicza konwertująca osobę na strukturę bajtową.

    :param osoba: lista zawierająca atrybuty opisujące osobę
    :return: struktura bajtowa
    """
    imie, nazwisko, plec, rok_urodzenia = osoba
    b_imie = imie.ljust(20).encode('utf-16')
    b_nazwisko = nazwisko.ljust(20).encode('utf-16')
    return struct.pack('40s40s?h', b_imie, b_nazwisko, plec, rok_urodzenia)


def serializuj(lista_osob, nazwa_pliku):
    """
    Funkcja dokonuje serializacji listy osób do strukturalnego pliku binarnego.

    :param lista_osob: lista osób
    :param nazwa_pliku: nazwa pliku, który będzie zawierał zserializowane dane
    :return: None
    """
    print('Początek serializacji...')
    with open(nazwa_pliku, mode='wb') as plik:
        for osoba in lista_osob:
            struktura_bajtow = __spakuj_do_struktury(osoba)
            plik.write(struktura_bajtow)
    print('Koniec serializacji...')
