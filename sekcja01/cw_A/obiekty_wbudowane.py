import builtins

_abs = builtins.abs  # zapamiętujemy oryginalną funkcję (działa dla wartości numerycznych)


def abs(wartosc):
    if isinstance(wartosc, str):  # gdy wartością jest tekst...
        return ''.join(sorted(set(wartosc)))
    return _abs(wartosc)  # w pozostałuch przypadkach - wywołanie oryginalne


builtins.abs = abs  # zamiana oryginalnej funkcji na nową


def test_dzialania_funkcji(funkcja, argument):
    try:
        print(f'{funkcja.__name__}({argument!r}) = ', end='')
        wynik = funkcja(argument)
        print(wynik)
    except TypeError as e:
        print(f'{e.__class__.__name__}: {e}')


if __name__ == '__main__':
    print('WYWOŁANIE ORYGINALNEJ FUNKCJI:')
    test_dzialania_funkcji(_abs, -7)
    test_dzialania_funkcji(_abs, 'Collegium Da Vinci')

    print('\nWYWOŁANIE NOWEJ FUNKCJI:')
    test_dzialania_funkcji(abs, -7)
    test_dzialania_funkcji(abs, 'Collegium Da Vinci')
