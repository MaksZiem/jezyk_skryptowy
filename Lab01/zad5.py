from datetime import datetime, date

data_str = input("Podaj datę w formacie rrrr-mm-dd: ")

data = datetime.strptime(data_str, '%Y-%m-%d').date()

liczba_dni = (date.today() - data).days

print("Liczba dni od podanej daty do dzisiaj wynosi:", liczba_dni)
