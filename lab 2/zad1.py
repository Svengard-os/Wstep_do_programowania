ilpunkt = int(input("Podaj ilość punktów zdobytych na egzaminie: "))
wynik = "Egzamin do poprawy"

if ilpunkt > 80:
    wynik = "Egzamin zaliczony w terminie zerowym"
elif ilpunkt >= 50:
    wynik = "Możliwa poprawa wyniku"

print(wynik)