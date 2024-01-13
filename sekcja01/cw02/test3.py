from sekcja01.cw02.importy.import3 import osoby

if __name__ == '__main__':
    print('OSOBY:')
    # Do konwersji instancji na tekst używana jest standardowo funkcja str()
    print(*osoby, sep='\n')
