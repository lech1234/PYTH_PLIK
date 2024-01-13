import datetime


class Osoba:
    """
    Klasa definiuje typ reprezentujący osobę.

    Klasa wykorzystuje właściwości. Do ich implementacji użyto dekoratorów.
    """

    def __init__(self, imie, nazwisko, plec, rok_urodzenia):
        """
        Metoda inicjująca właściwości.
        """
        self.imie = imie
        self.nazwisko = nazwisko
        self.plec = plec
        self.rok_urodzenia = rok_urodzenia

    # Metody dostępowe do odczytu atrybutów (gettery)
    @property
    def imie(self):
        return self.__imie

    @property
    def nazwisko(self):
        return self.__nazwisko

    @property
    def plec(self):
        return 'M' if self.__plec else 'K'

    @property
    def rok_urodzenia(self):
        return self.__rok_urodzenia

    # Metody dostępowe do ustawiania atrybutów (settery)
    @imie.setter
    def imie(self, imie):
        if imie:
            self.__imie = imie
        else:
            raise ValueError('....... Imię odrzucone (nie może być puste)')

    @nazwisko.setter
    def nazwisko(self, nazwisko):
        if nazwisko:
            self.__nazwisko = nazwisko
        else:
            raise ValueError('....... Nazwisko odrzucone (nie może być puste)')

    @plec.setter
    def plec(self, plec):
        if isinstance(plec, bool):
            self.__plec = plec
        else:
            raise TypeError('....... Płeć odrzucona (nie jest wartością logiczną)')

    @rok_urodzenia.setter
    def rok_urodzenia(self, rok_urodzenia):
        if rok_urodzenia < datetime.date.today().year:
            self.__rok_urodzenia = rok_urodzenia
        else:
            raise ValueError('....... Rok urodzenia odrzucony (jeszcze nie nadszedł)')

    def ile_lat(self):
        """
        Metoda oblicza aktualny wiek osoby.
        """
        return datetime.date.today().year - self.__rok_urodzenia

    def __str__(self):
        """
        Metoda konwersji obiektu osoby na postać tekstową (zwraca pełny opis obiektu)
        Przykład:
        Jan Kowalski, płeć: M, wiek: 29 lat(a)
        """
        return f'{self.imie} {self.nazwisko}, płeć: {self.plec}, wiek: {self.ile_lat()} lat(a)'


def utworz_osobe(imie, nazwisko, plec, rok_urodzenia):
    """
    Funkcja pomocnicza, która stara się utworzyć osobę i informuje o powodzeniu lub o problemach.

    :param imie: imię osoby
    :param nazwisko: nazwisko osoby
    :param plec: płeć osoby (True/False)
    :param rok_urodzenia: rok urodzenia osoby
    :return: instancja osoby lub wypisanie komunikatu o błędzie
    """
    try:
        osoba = Osoba(imie, nazwisko, plec, rok_urodzenia)
    except ValueError as e:
        print('WYJĄTEK:', e)
    except TypeError:
        print('WYJĄTEK: ....... Błędny typ danych')
    else:
        print('OK:     ', osoba)
        return osoba


if __name__ == '__main__':

    # Test
    utworz_osobe('Jan', 'Kowalski', True, 1990)  # poprawne utworzenie osoby
    utworz_osobe(None, 'Kowalski', True, 1990)  # błędne utworzenie osoby - brak imienia
    utworz_osobe('Jan', '', True, 1990)  # błędne utworzenie osoby - brak nazwiska
    utworz_osobe('Jan', 'Kowalski', 1, 1990)  # błędna wartość płci
    utworz_osobe('Jan', 'Kowalski', True, 2025)  # błędna wartość roku urodzenia
    utworz_osobe('Jan', 'Kowalski', True, '1990')  # błędna typ roku urodzenia
