# import pakiet.podpakiet.modul

# Tu muszą pozostać importy bezwzględne.
# Importy względne funkcjonują tylko dla importów typu: from ... import ...
import cw01_02.model.osoba
import cw01_02.model.adres as a

osoby = [
    cw01_02.model.osoba.Osoba('Jan', 'Kowalski',
                              a.Adres('ul. Morska 11', '12-345', 'Gdańsk')),
    cw01_02.model.osoba.Osoba('Adam', 'Bednarek',
                              a.Adres('ul. Polna 3', '23-456', 'Mrągowo')),
    cw01_02.model.osoba.Osoba('Anna', 'Jabłońska',
                              a.Adres('ul. Polska 42', '34-567', 'Kołobrzeg'))
]

if __name__ == '__main__':
    print('OSOBY:')
    print(*osoby, sep='\n')
