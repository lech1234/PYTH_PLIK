class TelefonNaKarte:
    """
    Klasa symuluje działanie telefonu na kartę.
    """

    def __init__(self, minuty_na_start):  # symulacja startera
        """
        Metoda inicjalizacyjna tworząca atrybuty instancyjne.

        :param minuty_na_start: początkowy stan na karcie (starter)

        Atrybut __minuty przechowuje aktualną liczbę minut do wykorzystania na rozmowy
        """
        self.__minuty = minuty_na_start

    def ile_minut_na_rozmowy(self):
        """
        Metoda informuje o bieżącym stanie minut na karcie.

        :return: liczba minut do wykorzystania na rozmowy
        """
        return self.__minuty

    def doladuj(self, dodatkowe_minuty):
        """
        Metoda umożliwia doładowanie na karcie.

        :param dodatkowe_minuty: liczba minut doładowania
        :return: None
        """
        self.__minuty += dodatkowe_minuty

    def rozmawiaj(self, czas_rozmowy):
        """
        Metoda reprezentuje rozmowę.

        :param czas_rozmowy: czas trwania rozmowy w minutach
        :return: None
        """
        print('Fajnie się rozmawiało...', end=' ')
        self.__minuty -= czas_rozmowy


if __name__ == '__main__':

    telefon = TelefonNaKarte(10)
    liczba_rozmow_do_wykonania = 10

    while liczba_rozmow_do_wykonania > 0:
        telefon.rozmawiaj(7)  # rozmowa

        # Doładowujemy konto mniejszą liczbą minut, niż trwa rozmowa,
        # co może doprowadzić do braku środków, czyli sytuacji wyjątkowej.
        # Program nie jest na to przygotowany i zapewne doprowadzi to
        # do ujemnego stanu konta... (będzie działał, tak jakby nic się nie stało)
        telefon.doladuj(5)  # doładowanie

        print(f'(Pozostało {telefon.ile_minut_na_rozmowy():3d} min na rozmowy)')  # ile minut pozostało?
        liczba_rozmow_do_wykonania -= 1
