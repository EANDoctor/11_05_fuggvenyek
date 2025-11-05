def szam_eldontese(x, y):
    if szam1 > szam2:
        print(f"A(z) {szam1} nagyobb mint {szam2}.")
    elif szam1 < szam2:
        print(f"A(z) {szam2} nagyobb mint {szam1}.")
    else:
        print("A két szám egyenlő.")

szam1 = int(input("Kérlek ajd meg egy számot!"))
szam2 = int(input("Kérlek ajd meg egy számot!"))
szam_eldontese(szam1, szam2)