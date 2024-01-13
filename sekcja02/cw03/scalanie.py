if __name__ == '__main__':
    # pliki wejściowe
    sciezka_we1 = '../teksty/tekst_en.txt'
    sciezka_we2 = '../teksty/tekst_pl.txt'
    # plik wyjściowy
    sciezka_wy = '../teksty/calosc.txt'

    with open(sciezka_wy, mode='wt', encoding='utf-8') as plik_wy:
        for sciezka_we in (sciezka_we1, sciezka_we2):
            with open(sciezka_we, mode='rt', encoding='utf-8') as plik_we:
                plik_wy.write(plik_we.read())  # kopiujemy cały plik za jednym razem, bo jest niewielki
                plik_wy.write('\n')
