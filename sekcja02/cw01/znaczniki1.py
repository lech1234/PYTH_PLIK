class Element:
    """
    Implementacja znacznika XML/HTML jako menedżera kontekstu z wykorzystaniem klasy.
    """

    def __init__(self, nazwa, **atrybuty):
        """
        Metoda inicjująca instancję.

        :param nazwa: nazwa elementu/znacznika
        :param atrybuty: atrybuty znacznika jako argumenty nazwane
        """
        self.nazwa = nazwa.upper()
        self.atrybuty = atrybuty

    def __enter__(self):
        """
        Metoda wywoływana podczas wykonywania instrukcji: with ...

        :return: instancja menedżera kontekstu
        """
        elementy_znacznika_poczatkowego = [self.nazwa]
        elementy_znacznika_poczatkowego += [f'{nazwa_atrybutu}="{wartosc_atrybutu}"'
                                            for nazwa_atrybutu, wartosc_atrybutu in self.atrybuty.items()]
        tresc_znacznika_poczatkowego = ' '.join(elementy_znacznika_poczatkowego)
        print(f'<{tresc_znacznika_poczatkowego}>')

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Metoda wywoływana przy kończeniu pracy z menedżerem kontekstu.

        :param exc_type: obiekt klasy wyjątku lub None
        :param exc_val: instancja wyjątku lub None
        :param exc_tb: ślad stosu wyjątku lub None
        :return: None
        """
        print(f'</{self.nazwa}>')


if __name__ == '__main__':
    with Element('html'):
        with Element('head'):
            with Element('meta', encoding='utf-8'):
                pass
            with Element('title'):
                print('Przykładowy prosty dokument HTML')
        with Element('body', color='white', width='80%'):
            print('Witaj w świecie Pythona!')
