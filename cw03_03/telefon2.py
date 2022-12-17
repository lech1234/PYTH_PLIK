class BrakMinut(Exception):
    """
    Nasz własny wyjątek sygnalizujący brak wystarczającej liczby minut na koncie na rozmowę.
    """
    def __init__(self, time_left):
        super().__init__(f'PROBLEM: Czas bieżącej rozmowy przekracza limit {time_left} min. na karcie')


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
        if self.__minuty < czas_rozmowy:
            raise BrakMinut(self.__minuty)
        print('Fajnie się rozmawiało...', end=' ')
        self.__minuty -= czas_rozmowy


if __name__ == '__main__':
    telefon = TelefonNaKarte(10)
    liczba_rozmow_do_wykonania = 10

    while liczba_rozmow_do_wykonania > 0:
        try:
            telefon.rozmawiaj(7)
        except BrakMinut as e:
            telefon.doladuj(5)
            print(f'{e} -> Doładowanie (teraz bieżący limit: {telefon.ile_minut_na_rozmowy()} min.)')
        else:
            print(f'(Pozostało {telefon.ile_minut_na_rozmowy()} min. na rozmowy)')
            liczba_rozmow_do_wykonania -= 1
