def test(wartosc):
    print(f'{wartosc!r:10} to ', end='')
    try:
        wartosc + 0
    except TypeError:
        try:
            wartosc + ''
        except TypeError:
            print('ani liczba, ani tekst')
        else:
            print('jakiś tekst')
    else:
        print('jakaś liczba')


if __name__ == '__main__':
    test(True)
    test('abc')
    test((1, 2))
