import contextlib as cl


@cl.contextmanager
def element(nazwa, **atrybuty):
    """
    Implementacja znacznika XML/HTML jako menedżera kontekstu z wykorzystaniem funkcji.

    :param nazwa: nazwa elementu/znacznika
    :param atrybuty: atrybuty znacznika jako argumenty nazwane
    :return: instancja menedżera kontekstu
    """
    nazwa = nazwa.upper()
    elementy_znacznika_poczatkowego = [nazwa]
    elementy_znacznika_poczatkowego += [f'{nazwa_atrybutu}="{wartosc_atrybutu}"'
                                        for nazwa_atrybutu, wartosc_atrybutu in atrybuty.items()]
    tresc_znacznika_poczatkowego = ' '.join(elementy_znacznika_poczatkowego)
    print(f'<{tresc_znacznika_poczatkowego}>')
    yield
    print(f'</{nazwa}>')


if __name__ == '__main__':
    with element('html'):
        with element('head'):
            with element('meta', encoding='utf-8'):
                pass
            with element('title'):
                print('Przykładowy prosty dokument HTML')
        with element('body', color='white', width='80%'):
            print('Witaj w świecie Pythona!')
