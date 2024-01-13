class Osoba:
    def __init__(self, imie, nazwisko, adres):
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__adres = adres

    def __str__(self):
        return f'{self.__imie} {self.__nazwisko}, zam.: {self.__adres!s}'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__imie}', '{self.__nazwisko}', {self.__adres!r})"
