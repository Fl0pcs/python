#Anna muutuja väärtuseks list kolmest oma lemmik puuviljast ja väljasta see
#Väljasta listi esimene väärtus
#Lisa listi lõppu uus puuvili
#Väljasta listi viimane väärtus
#Muuda ühe elemendi väärtust ja väljasta kogu list
#Kontrolli kas väärtus (näiteks õun) eksisteerib listis
#Väljasta listi pikkus
##Eemalda listist element ja väljasta kogu list
#Muuda listi järjekord vastupidiseks
#Sorteeri list ja väljasta
#(jada, list, listi element, listi meetodid)

fruits = ["mango", "ananass", "pirn"]
print(fruits)

print(fruits[0])

fruits.append("õun")
print(fruits[-1])

fruits[1] = "apelsin"
print(fruits)

if "õun" in fruits:
    print("Õun on listis")
else:
    print("Õuna pole listis")

print(len(fruits))

fruits.remove("pirn")
print(fruits)

fruits.reverse()
print(fruits)

fruits.sort()
print(fruits)

