def histogram_znakow(sciezka):
    histogram = {}

    with open(sciezka, "r") as plik:
        for linia in plik:
            for znak in linia:
                if znak in histogram:
                    histogram[znak] += 1
                else:
                    histogram[znak] = 1

    return histogram


print(histogram_znakow("document.txt"))