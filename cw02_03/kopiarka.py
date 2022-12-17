path_to_resources = '../lyrics/'

with open(path_to_resources + 'calosc.txt', mode='wt', encoding='utf-8') as outfile:
    for filename in ('tekst_en.txt', 'tekst_pl.txt'):
        with open(path_to_resources + filename, mode='rt', encoding='utf-8') as infile:
            outfile.write(infile.read())
            outfile.write('\n')
