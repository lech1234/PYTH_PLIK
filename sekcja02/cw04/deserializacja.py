"""
Moduł zawiera funkcje umożliwiające deserializację.
"""
from sekcja01.model.osoba import Osoba
from sekcja01.model.adres import Adres


def deserializuj(nazwa_pliku):
    """
    Funkcja dokonuje deserializacji obiketu z pliku w formacie tekstowym.

    :param nazwa_pliku: nazwa pliku tekstowego zawierającego zserializowaną listę osób
    :return: odtworzona lista osób

    Do deserializacja została użyta funkcja eval.
    """
    print('Początek deserializacji...')
    with open(nazwa_pliku, mode='rt', encoding='utf-8') as plik:
        lista = list(map(eval, plik))
    print('Koniec deserializacji...')
    return lista
