import random

n = int(input("Podaj liczbę elementów tablicy: "))
array = []

for i in range(n):
    liczba = random.randint(-5, 5)
    array.append(liczba)

print("Tablica: ", array)

with open("result.txt", "w") as plik:
    for liczba in array:
        plik.write(str(liczba) + "\n")

print("Tablica zapisana do pliku.")
