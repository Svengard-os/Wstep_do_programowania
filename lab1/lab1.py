#Zad. 1:

#1.1.1. 1 + 2 <class 'int'> Dodawanie
a = 1 + 2
print (type(a))
#1.1.2. 1 + 4.5 <class 'float'> Dodawanie
a = 1 + 4.5
print (type (a))
#1.1.3. 3 / 2 <class 'float'> Dzielenie zmiennoprzecinkowe
a = 3/2
print(type(a))
#1.1.4. 4 / 2 <class 'float'> Dzielenie zmiennoprzecinkowe
a = 4 / 2
print (type(a))
#1.1.5. 3 // 2 <class 'int'> Dzielenie całkowite
a = 3 // 2
print(type(a))
#1.1.6. -3 // 2 <class 'int'> Dzielenie całkowite
a = -3 // 2
print (type(a))
#1.1.7. 11 % 2 <class 'int'> Dzielenie modulo (reszta z dzielenia)
a = 11 % 2
print (type(a))
#1.1.8. 2 ** 10 <class 'int'>  Potęgowanie
a = 2** 10
print(type(a))
#1.1.9. 8 ** (1/3) <class 'float'> Potęgowanie
a = 8 ** (1/3)
print (type(a))

#1.2
int(3.0) #liczba zmiennoprzecinkowa--->liczba całkowita
float(3) #liczba całkowita---->liczba zmiennoprzecinkowa
float("3") #ciąg znaków---->liczba zmiennoprzecinkowa
str(12.4) #liczba zmiennoprzecinkowa---->ciąg znaków
bool(0) #liczba całkowita---->wartość logiczna False

#Zad. 2:

uczelnia = "Studiuję na WSIiZ"
print(uczelnia)

#Zad. 3:

imię = 'Jan'
wiek = 20
wzrost = 178

print (f"Nazywam się {imię} i mam {wiek} lat. \nMój wzrost to {wzrost} cm.")

#Zad. 4:

Cena = 39.99
Rabat = 0.2
zrabatem = Cena - (Cena*Rabat)

print(f"Cena przecenionego produktu:: {zrabatem:.2f} złotych")

#Zad. 5:

#dane
a = float(input("Podaj długość boku a: "))
b = float(input("Podaj długość boku b: "))

#wzory
p = a*b
o = (2*a)+(2*b)

#tekst wynik
print(f"Pole: {p}")
print(f"Obwód: {o}")

#Zad. 6:

#dane
drogainpt = float(input("Podaj drogę pokonaną w km:"))
srspal = float(input("Podaj średnie zużycie paliwa samochodu: "))

#obliczenia
spalane = (drogainpt*srspal)/100
koszt = srspal * 6.5

#tekst wynik
print(f"Ilość zużytego paliwa: {round(spalane, 2)} litrów")
print(f"Przewidywane koszta podróży: {round(koszt, 2)} złotych")

#6.1

#losowe
import random
drogalos = random.randint(1, 544)

#dane
paliwo = float(input("Podaj cenę paliwa:"))
srspal = float(input("Podaj średnie zużycie paliwa samochodu:"))

#obliczenia
spalane = (drogalos*srspal)/100
koszt = srspal + spalane

#tekst wynik
print(f"Zużycie paliwa za odcinku {drogalos} kilometrów wyniesie: {round(spalane, 2)} litrów")
print(f"Koszt podróży: {round(koszt, 2)} złotych")

#6.2
#moje funkcje print() już korzystają z f-stringów