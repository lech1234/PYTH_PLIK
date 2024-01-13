"""
Moduł prezentuje działanie asercji.

Uruchom go z wiersza poleceń...
1. bez optymalizacji:
   python ./sekcja03/cw_A/asercje.py

2. z opcją optymalizacji:
   python -O ./sekcja03/cw_A/asercje.py
"""

n = 13  # wartość losowana lub wyliczana przez program

# Chcemy przekonać się jak się zachowa program w przypadku otrzymania takie niespodziewanej wartości
if __debug__:
    def czy_szczesliwa(liczba):
        return liczba != 13

    # testujemy stan - jesteśmy przekonani, że n ma wartość inną niż 13
    assert czy_szczesliwa(n), 'wylosowałeś 13'

print('Twoja szczęśliwa liczba to', n)
