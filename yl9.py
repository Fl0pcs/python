#Kolmnurki liigitatakse külgede pikkuse järgi erikülgseteks, võrdhaarseteks ja
#võrdkülgseteks. Kirjutada programm, mis küsib kasutajalt kolme külje pikkused
#ning väljastab vastusena kolmnurga liigi. Lisaks tuleb kontrollida, kas etteantud 
#küljepikkustega kolmnurk saab üldse eksisteerida. Külje pikkused ei pea olema 
#täisarvud. (ujukomaarv - float)

# Triangle classifier by side lengths (float)
# Asks user for three side lengths, checks if a triangle is possible,
# then prints the triangle type in Estonian.

def almost_equal(x, y, eps=1e-9):
    """Return True if x and y are equal within a small tolerance."""
    return abs(x - y) <= eps

a = float(input("Sisesta esimese külje pikkus: "))
b = float(input("Sisesta teise külje pikkus: "))
c = float(input("Sisesta kolmanda külje pikkus: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Külje pikkused peavad olema positiivsed.")
else:
    eps = 1e-9
    if (a + b <= c + eps) or (a + c <= b + eps) or (b + c <= a + eps):
        print("Selliste külgedega kolmnurk ei saa eksisteerida.")
    else:
        if almost_equal(a, b) and almost_equal(b, c):
            print("Tegu on võrdkülgse kolmnurgaga.")
        elif almost_equal(a, b) or almost_equal(a, c) or almost_equal(b, c):
            print("Tegu on võrdhaarse kolmnurgaga.")
        else:
            print("Tegu on erikülgse kolmnurgaga.")
