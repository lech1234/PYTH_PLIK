class Adres:
    """
    Klasa modelu reprezentująca adres osoby.
    """

    def __init__(self, ulica, kod_pocztowy, miejscowosc):
        """
        Metoda konstruktorowa tworząca nową instancję adresu.

        :param ulica: nazwa ulicy (tekst)
        :param kod_pocztowy: kod pocztowy (tekst)
        :param miejscowosc: nazwa miejscowości (tekst)
        """
        self.__ulica = ulica
        self.__kod_pocztowy = kod_pocztowy
        self.__miejscowosc = miejscowosc

    def __str__(self):
        """
        Metoda konwersji adresu na tekst.

        :return: importy adresu w postaci: <ulica>, <kod pocztowy> <miejscowosc>
        """
        return f'{self.__ulica}, {self.__kod_pocztowy} {self.__miejscowosc}'

    def __repr__(self):
        """
        Metoda konwersji adresu na tekst.

        :return: adres w postaci: Adres('<ulica>', '<kod pocztowy>', '<miejscowosc>')
        """
        return f"{self.__class__.__name__}('{self.__ulica}', '{self.__kod_pocztowy}', '{self.__miejscowosc}')"

    def __eq__(self, other):
        """
        Implementacja operatora porównania (==).

        :param other: obiekt do porównania z bieżącym (self)
        :return: wynik porównania
        """
        return (self.__class__ == other.__class__
                and self.__ulica == other.__ulica
                and self.__kod_pocztowy == other.__kod_pocztowy
                and self.__miejscowosc == other.__miejscowosc)


if __name__ == '__main__':
    # Test klasy Adres
    # Ten kod powinien być wykonany tylko z tego modułu (nie powinien być wykonywany podczas importu)

    adres = Adres('ul. Bracka 1', '12-345', 'Kraków')
    print(str(adres))
    print(repr(adres))
