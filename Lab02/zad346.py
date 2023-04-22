import math

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
def pole_kola(promien):
    wynik = math.pi * promien ** 2
    out = "pole wynosi "+str(wynik)
    with open("wynik.txt", "w") as file:
        file.write(out)
    return wynik

def obwod_kola(promien):
    wynik = 2 * math.pi * promien
    out = "obwod wynosi " + str(wynik)
    with open("wynik.txt", "w") as file:
        file.write(out)
    return wynik

print("Wybierz działanie:")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnożenie")
print("4. Dzielenie")
print("5. Pole koła")
print("6. Obwód koła")

wybor = input("Wybierz opcję (1/2/3/4/5/6): ")

if wybor in ['1', '2', '3', '4']:
    liczba1 = float(input("Podaj pierwszą liczbę: "))
    liczba2 = float(input("Podaj drugą liczbę: "))

    if wybor == '1':
        print(liczba1, "+", liczba2, "=", dodawanie(liczba1, liczba2))
    elif wybor == '2':
        print(liczba1, "-", liczba2, "=", odejmowanie(liczba1, liczba2))
    elif wybor == '3':
        print(liczba1, "*", liczba2, "=", mnozenie(liczba1, liczba2))
    elif wybor == '4':
        print(liczba1, "/", liczba2, "=", dzielenie(liczba1, liczba2))
elif wybor == '5':
    promien = float(input("Podaj promień koła: "))
    print("Pole koła o promieniu", promien, "wynosi", pole_kola(promien))
elif wybor == '6':
    promien = float(input("Podaj promień koła: "))
    print("Obwód koła o promieniu", promien, "wynosi", obwod_kola(promien))
else:
    print("Błąd: Nieprawidłowa opcja")
