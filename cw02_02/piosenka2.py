path_to_resources = '../lyrics/'

with open(path_to_resources + 'tekst_en.txt', mode='rt', encoding='utf-8') as file1, \
        open(path_to_resources + 'tekst_pl.txt', mode='rt', encoding='utf-8') as file2:
    for line1, line2 in zip(file1, file2):
        print(line1, line2, sep='', end='')
