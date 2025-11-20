#Kirjuta programm, mis leiab kolmest kasutaja poolt sisestatud arvust 
# maksimumi (ära kasuta max funktsiooni). (loogikatehted - logic operators)

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a > b and a > c : 
    print("A on maksimum!", a)
elif b > c : 
    print("B on maksimum!", b)
else : 
    print("C on maksimum!", c)




