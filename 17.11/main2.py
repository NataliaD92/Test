# Zadanie 1.5

# x = int(input("Wprowadź liczbę"))
# result = x / 2 + 4
# # Sprawdźmy czy otrzymaliśmy poprawny wynik
# assert result == 14

# ----------------------------------

# Zadanie 2.1

# name = input("Wprowadź imię ")
# lastname = input("Wprowadź nazwisko ")

# print(f"Cześć {lastname} {name}")

# ----------------------------------

# Zadanie 2.2

# file_name = input("Wprowadź nazwę pliku:\n")

# print(f"Rozszerzenie pliku to: {file_name.split(".")[1]}")

# ----------------------------------

# Zadanie 2.3

# day = input("Wprowadź dzień wydarzenia:\n")
# month = input("Wprowadź miesiąc wydarzenia:\n")
# year = input("Wprowadź rok wydarzenia:\n")

# print(f"{day}/{month}/{year}")

# ----------------------------------

# Zadanie 2.4

# x = int(input("Wprowadź pierwszą liczbę:\n"))
# y = int(input("Wprowadź drugą liczbę:\n"))

# print(f"Suma {x} oraz {y} to {x+y}")


# ----------------------------------

# Zadanie 2.5

# a = int(input("Wprowadź pierwszą liczbę całkowitą: "))
# b = int(input("Wprowadź drugą liczbę całkowitą: "))
# c = float(input("Wprowadź pierwszą liczbę zmiennoprzecinkową: "))
# d = float(input("Wprowadź drugą liczbę zmiennoprzecinkową: "))

# wynik1 = a+c
# wynik2 = d-b

# print(f"Wynik operacji 1: {wynik1}")
# print(type(wynik1))
# print(f"Wynik operacji 2: {wynik2}")
# print(type(wynik2))

# suma = wynik1 + wynik2

# print(f"Suma to: {suma}")
# print(type(suma))

# ----------------------------------

# Zadanie 2.6

# liczba = int(input("Wprowadź liczbę: "))
# pierwiastek = int(input("Wprowadź stopień pierwiastka: "))

# wynik = liczba**(1/pierwiastek)
# print(wynik)

# ----------------------------------

# Zadanie 2.7

# napis1 = input("Podaj napis 1:\n")
# napis2 = input("Podaj napis 2:\n")

# print(napis1,napis2)
# print(f"{napis1} {napis2}")
# print(napis1, end=" ")
# print(napis2)
# print(napis1 + " " + napis2)

# ----------------------------------

# Zadanie 2.8

# a = float(input("Wprowadź pierwszy bok: "))
# b = float(input("Wprowadź drugi bok: "))
# c = float(input("Wprowadź trzeci bok: "))

# p= 1/2*(a+b+c)

# pole = (p*(p-a)*(p-b)*(p-c))**(1/2)

# print(f"Pole trójkąta wynosi: {pole:.2f}")

# ----------------------------------

# Zadanie 2.9

# km = float(input("Wprowadź wartość w kilometrach: "))

# print(f"{km} kilometra to {km*0.621371192:.2f} mili")

# ----------------------------------

# Zadanie 2.10

cel = int(input("Wprowadź temperaturę w stopniach Cejsjusza: "))
fahr = (cel*9/5)+32

print(f"{cel} stopni Celsjusza to {fahr:.0f} stopni Fahrenheita.")