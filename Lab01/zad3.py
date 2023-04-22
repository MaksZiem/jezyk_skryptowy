suma = 0

liczba = input("Podaj liczbę całkowitą (lub wpisz 'stop' aby zakończyć): ")

while liczba != "stop":
    suma += int(liczba)
    liczba = input("Podaj liczbę całkowitą (lub wpisz 'stop' aby zakończyć): ")

print("Suma liczb całkowitych: ", float(suma))
