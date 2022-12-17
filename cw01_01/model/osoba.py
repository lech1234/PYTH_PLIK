class Osoba:
    def __init__(self, imie, nazwisko, adres):
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__adres = adres

    def __str__(self):
        return f'{self.__imie} {self.__nazwisko}, zam.: {self.__adres!s}'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__imie}', '{self.__nazwisko}', {self.__adres!r})"

if __name__ == '__main__':
    import adres
    adres1 = adres.Adres('ul. Bracka 1', '12-345', 'Kraków')
    osoba1 = Osoba('Jan', 'Kowalski', adres1)

    print(str(osoba1))
    print(repr(osoba1))
