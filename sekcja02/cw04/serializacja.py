"""
Moduł zawiera funkcje umożliwiające serializację.
"""
def serializuj(nazwa_pliku, lista_osob):
    """
    Funkcja dokonuje serializacji podanego obiektu do pliku w formacie tekstowym.

    :param nazwa_pliku: nazwa pliku z wynikiem serializacji
    :param lista_osob: lista instancji typu Osoba
    :return: None

    Do serializacji została użyta funkcja repr.
    Format zserializowanego obiektu Osoba:
    Osoba('imię', 'nazwisko', Adres('ulica', 'kod pocztowy', 'miejscowość'))

    """
    print('Początek serializacji...')
    with open(nazwa_pliku, mode='wt', encoding='utf-8') as file:
        for osoba in lista_osob:
            file.write(f'{osoba!r}\n')  # konwersja osoba -> repr(osoba)
    print('Koniec serializacji...')
