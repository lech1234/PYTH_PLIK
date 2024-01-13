if __name__ == '__main__':
    sciezka1 = '../teksty/tekst_en.txt'
    sciezka2 = '../teksty/tekst_pl.txt'

    for sciezka in (sciezka1, sciezka2):
        jezyk = sciezka[-6:-4].upper()
        with open(sciezka, mode='rt', encoding='utf-8') as plik:
            for linia in plik:  # plik jest iterowalny, odczyt linia po linii
                print(f'[{jezyk}]: {linia}', end='')
