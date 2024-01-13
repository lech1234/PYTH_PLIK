"""
Moduł zawiera funkcje umożliwiające deserializację.
"""
import io
import struct


def __wypakuj_ze_struktury(struktura):
    """
    Funkcja pomocnicza konwertująca strukturę bajtów na listę atrybutów opisujących osobę
    :param struktura: struktura bajtów
    :return: lista opisująca osobę
    """
    b_imie, b_nazwisko, plec, rok_urodzenia = struct.unpack('40s40s?h', struktura)
    imie = b_imie.decode('utf-16').strip()
    nazwisko = b_nazwisko.decode('utf-16').strip()
    return [imie, nazwisko, plec, rok_urodzenia]


def deserializuj_wszystkie_osoby(nazwa_pliku):
    """
    Funkcja deserializuje listę osób ze strukturalnego pliku binarnego.

    :param nazwa_pliku: nazwa pliku zawierającego strukturalne dane binarne
    :return: lista osób
    """
    print('Początek deserializacji...')
    rozmiar_struktury = struct.calcsize('40s40s?h')
    with open(nazwa_pliku, mode='rb') as plik:
        lista_osob = []
        while struktura_bajtow := plik.read(rozmiar_struktury):
            osoba = __wypakuj_ze_struktury(struktura_bajtow)
            lista_osob.append(osoba)
    print('Koniec deserializacji...')
    return lista_osob


def deserializuj_osobe(nazwa_pliku, nr_rekordu):
    """
    Funkcja deserializuje wybraną osobę ze strukturalnego pliku binarnego.

    :param nazwa_pliku: nazwa pliku zawierającego strukturalne dane binarne
    :param nr_rekordu: numer osoby
    :return: lista opisująca wybraną osobę
    """
    print('Początek deserializacji...')
    rozmiar_struktury = struct.calcsize('40s40s?h')
    with open(nazwa_pliku, mode='rb') as file:
        file.seek(rozmiar_struktury * nr_rekordu, io.SEEK_SET)
        bytes_struct = file.read(rozmiar_struktury)
        osoba = __wypakuj_ze_struktury(bytes_struct)
    print('Koniec deserializacji...')
    return osoba
