class Osoba:
    """
    Klasa modelu reprezentująca osobę.
    """

    def __init__(self, imie, nazwisko, adres):
        """
        Metoda konstruktorowa tworząca nową instancję osoby.

        :param imie: imię osoby (tekst)
        :param nazwisko: nazwisko osoby (tekst)
        :param adres: adres osoby (instancja typu Adres)
        """
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__adres = adres

    def __str__(self):
        """
        Metoda konwersji adresu na tekst.

        :return: importy osoby w postaci: <imie> <nazwisko>, zam. <adres>
        """
        return f'{self.__imie} {self.__nazwisko}, zam.: {self.__adres!s}'

    def __repr__(self):
        """
         Metoda konwersji osoby na tekst.

        :return: osoba w postaci: Osoba('<imie>', '<nazwisko>', <adres>)
        """
        return f"{self.__class__.__name__}('{self.__imie}', '{self.__nazwisko}', {self.__adres!r})"

    def __eq__(self, other):
        """
        Implementacja operatora porównania (==).

        :param other: obiekt do porównania z bieżącym (self)
        :return: wynik porównania
        """
        return (self.__class__ == other.__class__
                and self.__imie == other.__imie
                and self.__nazwisko == other.__nazwisko
                and self.__adres == other.__adres)


if __name__ == '__main__':
    # Test klasy Osoba
    # Ten kod powinien być wykonany tylko z tego modułu (nie powinien być wykonywany podczas importu)
    import adres

    adres1 = adres.Adres('ul. Bracka 1', '12-345', 'Kraków')
    osoba1 = Osoba('Jan', 'Kowalski', adres1)

    print(str(osoba1))
    print(repr(osoba1))
