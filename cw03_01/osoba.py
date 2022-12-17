import datetime


class Osoba:
    """
    Klasa reprezentuje osoby.

    W klasie zdefiniowano właściwości.
    """

    def __init__(self, imie, nazwisko, plec, rok_urodzenia):
        self.imie = imie
        self.nazwisko = nazwisko
        self.plec = plec
        self.rok_urodzenia = rok_urodzenia

    # -------------------------------------------------------
    # Metody dostępowe do odczytu atrybutów - gettery
    # -------------------------------------------------------
    @property
    def imie(self):
        return self.__imie

    @property
    def nazwisko(self):
        return self.__nazwisko

    # Metoda zwraca informację o płci: M - mężczyzna, K - kobieta
    @property
    def plec(self):
        return "M" if self.__plec else "K"

    @property
    def rok_urodzenia(self):
        return self.__rok_urodzenia

    # -------------------------------------------------------
    # metody dostępowe do ustawiania atrybutów - settery
    # -------------------------------------------------------

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

    # Metoda konwersji obiektu osoby na postać tekstową (zwraca pełny opis obiektu)
    def __str__(self):
        return f'{self.imie} {self.nazwisko}, płeć: {self.plec}, wiek: {self.ile_lat()} lat'

    def ile_lat(self):
        return datetime.date.today().year - self.__rok_urodzenia


# Funkcja pomocnicza
# Próbuje utworzyć osobę i informuje o powodzeniu lub o problemach
def utworz_osobe(imie, nazwisko, plec, rok_urodzenia):
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
    osoba1 = utworz_osobe('Jan', 'Kowalski', True, 1990)  # poprawne utworzenie osoby
    osoba2 = utworz_osobe(None, 'Kowalski', True, 1990)  # błędne utworzenie osoby - brak imienia
    osoba3 = utworz_osobe('Jan', '', True, 1990)  # błędne utworzenie osoby - brak nazwiska
    osoba4 = utworz_osobe('Jan', 'Kowalski', 1, 1990)  # błędna wartość płci
    osoba5 = utworz_osobe('Jan', 'Kowalski', True, 2025)  # błędna wartość roku urodzenia
    osoba6 = utworz_osobe('Jan', 'Kowalski', True, '1990')  # błędna typ roku urodzenia
