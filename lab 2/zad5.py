#5.a

with open("notowania_gieldowe.txt", "r") as plik:
    for linia in plik:
        print(linia.strip())

#5.b

with open("notowania_gieldowe.txt", "a") as plik:
    plik.write("\nALR, 113")

with open("notowania_gieldowe.txt", "r") as plik:
    for linia in plik:
        print(linia.strip())