class TelefonNaKarte:
    """
    Klasa symuluje działanie telefonu na kartę.

    atrybut __minuty: przechowuje aktualny stan minut do wykorzystania
    """

    def __init__(self, minuty_na_start):  # symulacja startera
        self.__minuty = minuty_na_start

    def ile_minut_na_rozmowy(self):  # odczyt bieżącego stanu konta (ilości minut do wykorzystania)
        return self.__minuty

    def doladuj(self, dodatkowe_minuty):  # doładowanie konta
        self.__minuty += dodatkowe_minuty

    def rozmawiaj(self, czas_rozmowy):  # rozmowa
        print('Fajnie się rozmawiało...', end=' ')
        self.__minuty -= czas_rozmowy


if __name__ == '__main__':
    telefon = TelefonNaKarte(10)
    liczba_rozmow_do_wykonania = 10

    while liczba_rozmow_do_wykonania > 0:
        telefon.rozmawiaj(7)  # rozmowa

        # Doładowujemy konto mniejszą liczbą minut, niż trwa rozmowa,
        # co może doprowadzić do braku środków, czyli sytuacji wyjątkowej.
        # Program nie jest na to przygotowany i zapewne doprowadzi
        # do ujemnego stanu konta... (będzie działał, tak jakby nic się nie stało)
        telefon.doladuj(5)  # doładowanie

        print(f'(Pozostało {telefon.ile_minut_na_rozmowy():3d} min na rozmowy)')  # ile minut pozostało?
        liczba_rozmow_do_wykonania -= 1
