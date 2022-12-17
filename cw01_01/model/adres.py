class Adres:
    def __init__(self, ulica, kod_pocztowy, miejscowosc):
        self.__ulica = ulica
        self.__kod_pocztowy = kod_pocztowy
        self.__miejscowosc = miejscowosc

    def __str__(self):
        return f'{self.__ulica}, {self.__kod_pocztowy} {self.__miejscowosc}'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__ulica}', '{self.__kod_pocztowy}', '{self.__miejscowosc}')"


if __name__ == '__main__':
    # test klasy
    # kod powinien być wykonany tylko z tego modułu (nie powinien być wykonywany podczas importu)

    adres = Adres('ul. Bracka 1', '12-345', 'Kraków')
    print(str(adres))
    print(repr(adres))
