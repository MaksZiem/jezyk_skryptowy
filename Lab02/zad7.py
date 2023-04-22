def funkcjaKwadratowa(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return "Brak rozwiązań rzeczywistych."
    elif delta == 0:
        x = -b / (2 * a)
        return f"Jedno podwójne rozwiązanie: x = "+str(x)+"."
    else:
        x1 = (-b - delta ** 0.5) / (2 * a)
        x2 = (-b + delta ** 0.5) / (2 * a)
        return "Dwa rozwiązania: x1 = "+str(x1)+", x2 = "+str(x2)+"."

a = 1
b = 2
c = -3
result = funkcjaKwadratowa(a, b, c)
with open("result.txt", "w") as file:
    file.write(result)
