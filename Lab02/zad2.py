import random

def randLiczby():
    liczby = []
    while len(liczby) < 6:
        liczba = random.randint(1, 49)
        if liczba not in liczby:
            liczby.append(liczba)
    return liczby


print(randLiczby())