n = int(input("Podaj liczbę elementów tablicy: "))
array = []

for i in range(n):
    sign = input(f"Podaj znak dla elementu {i}: ")
    array.append(sign)

print("Tablica przed odwróceniem: ", array)

reverseArray = list(reversed(array))

print("Tablica po odwróceniu: ", reverseArray)
