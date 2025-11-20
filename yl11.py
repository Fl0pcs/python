s = input("Sisesta string: ")

s = s.strip()

pikkus = len(s)

if pikkus < 7:
    print("String peab sisaldama vähemalt 7 sümbolit!")
elif pikkus % 2 == 0:
    print("Sümbolite arv peab olema paaritu!")
else:
    kesk_indeks = pikkus // 2
    kolm_keskmist = s[kesk_indeks - 1 : kesk_indeks + 2]

    print("Kolm keskmist sümbolit on:", kolm_keskmist)
