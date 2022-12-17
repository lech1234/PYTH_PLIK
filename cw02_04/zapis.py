from cw01_01.dane.osoby1 import osoby as persons

print('Początek serializacji...')
with open('osoby.txt', mode='wt', encoding='utf-8') as file:
    for person in persons:
        file.write(f'{person!r}\n')  # konwersja osoba -> repr(osoba)

print('Gotowe...')
