def dodawanie(a, b):
    return a + b
def odejmowanie(a, b):
    return a - b
def mnozenie(a, b):
    return a * b
def dzielenie(a, b):
    if b == 0:
        print("Nie można dzielić przez zero!")
    else:
        return a / b

print("Wybierz działanie:")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnożenie")
print("4. Dzielenie")

wybor = int(input("Wybierz opcję (1/2/3/4): "))

a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))

if wybor == 1:
    wynik = dodawanie(a, b)
    print("Wynik dodawania:", wynik)
elif wybor == 2:
    wynik = odejmowanie(a, b)
    print("Wynik odejmowania:", wynik)
elif wybor == 3:
    wynik = mnozenie(a, b)
    print("Wynik mnożenia:", wynik)
elif wybor == 4:
    wynik = dzielenie(a, b)
    if wynik is not None:
        print("Wynik dzielenia:", wynik)
else:
    print("Nieprawidłowy wybór działania!")
