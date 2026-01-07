#Kirjuta programm, mis küsib kasutajalt failinime kujul “failinimi.ext”
# (ext - extension - faili laiend) ja prindib välja laiendi (“ext”). (str.split)

filename = input("Sisesta failinimi (nt fail.ext): ")

osad = filename.split(".")

laiend = osad[-1]

print("Faili laiend on:", laiend)
