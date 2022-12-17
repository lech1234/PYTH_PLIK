from cw01_01.model.osoba import Osoba
from cw01_01.model.adres import Adres

print('Początek deserializacji...')
with open('osoby.txt', mode='rt', encoding='utf-8') as file:
    lista = list(map(eval, file))
print('Gotowe...')

print(*lista, sep='\n')
