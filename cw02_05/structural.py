import io
import struct


def __pack_to_struct(person_list):
    first_name, last_name, gender, birth_year = person_list
    b_first_name = bytes(first_name.ljust(20), 'utf-16')
    b_last_name = bytes(last_name.ljust(20), 'utf-16')
    return struct.pack('40s40s?h', b_first_name, b_last_name, gender, birth_year)


def __unpack_from_struct(bytes_struct):
    b_first_name, b_last_name, gender, birth_year = struct.unpack('40s40s?h', bytes_struct)
    first_name = b_first_name.decode('utf-16').strip()
    last_name = b_last_name.decode('utf-16').strip()
    return list((first_name, last_name, gender, birth_year))


def save_persons(persons_list, filename):
    with open(filename, mode='wb') as outfile:
        for person_list in persons_list:
            bytes_struct = __pack_to_struct(person_list)
            outfile.write(bytes_struct)


def read_persons(filename):
    n = struct.calcsize('40s40s?h')
    with open(filename, mode='rb') as infile:
        persons_list = []
        while True:
            bytes_struct = infile.read(n)
            if not bytes_struct:
                break
            person_list = __unpack_from_struct(bytes_struct)
            persons_list.append(person_list)
    return persons_list


def read_person(filename, record_no):
    length = struct.calcsize('40s40s?h')
    with open(filename, mode='a+b') as file:
        file.seek(length * record_no, io.SEEK_SET)
        bytes_struct = file.read(length)
        person_list = __unpack_from_struct(bytes_struct)
    return person_list


if __name__ == '__main__':
    # utworzenie listy osób
    persons = [
        ['Jan', 'Kowalski', True, 1990],
        ['Anna', 'Nowakowska', False, 2000]
    ]

    # zapis danych osób w formie strukturalnej do pliku binarnego
    save_persons(persons, 'osoby.dat')

    # odczyt wszystkich osób z pliku binarnego
    print('WSZYSTKIE OSOBY:')
    persons = read_persons('osoby.dat')
    print(*persons, sep='\n')

    # odczyt danych osoby ze strukturalnego pliku binarnego na podstawie nr rekordu
    print('OSOBA #2:')
    person = read_person('osoby.dat', 1)  # numeracja rekordów zaczyna się od zera
    print(person)
