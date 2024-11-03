
x = int(input("Podaj 1szą liczbę: x "))

y = int(input("Podaj 2gą liczbę: y "))

z = int(input("Podaj 3cią liczbę: z "))


if x > y:
    x, y = y, x

if x > z:
    x, z = z, x

if y > z:
    y, z = z, y

print("Liczby w kolejności od najmniejszej do największej:", x, y, z)