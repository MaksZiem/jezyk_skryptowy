# lista = [1,2,3,4]

def suma(list):
    suma = 0
    for liczba in list:
        suma+=liczba
    return suma

def funkcja2(funkcja2):
    with open("zad5file.txt", 'r') as plik:
        liczby = []
        for linia in plik:
            liczba = int(linia.strip())
            liczby.append(liczba)

    wynik = funkcja2(liczby)
    return  wynik

print(funkcja2(suma))