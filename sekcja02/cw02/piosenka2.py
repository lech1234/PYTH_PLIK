if __name__ == '__main__':
    sciezka1 = '../teksty/tekst_en.txt'
    sciezka2 = '../teksty/tekst_pl.txt'

    with (open(sciezka1, mode='rt', encoding='utf-8') as plik1,
          open(sciezka2, mode='rt', encoding='utf-8') as plik2):
        jezyk1 = sciezka1[-6:-4].upper()
        jezyk2 = sciezka2[-6:-4].upper()
        for linia1, linia2 in zip(plik1, plik2):
            print(f'[{jezyk1}]: {linia1}', end='')
            print(f'[{jezyk2}]: {linia2}', end='')
