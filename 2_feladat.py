def szam_eldontese(num):
    if num < 0:
        print("A megadott szám negatív.")
    elif num > 0:
        print("A megadott szám pozitív.")
    else:
        print("A megadott szám nulla")

szam = int(input("Kérlek ajd meg egy számot!"))
szam_eldontese(szam)