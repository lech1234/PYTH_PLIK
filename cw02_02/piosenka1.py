path_to_resources = '../lyrics/'

for file_name in ('tekst_en.txt', 'tekst_pl.txt'):
    with open(path_to_resources + file_name, mode='rt', encoding='utf-8') as file:
        for linia in file:  # plik jest iterowalny, odczyt linia po linii
            print(linia, end='')