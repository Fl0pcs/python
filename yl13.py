#Küsi kasutajalt lemmikloom. Väljasta selle muutuja esimene täht.
#Koosta list, mis koosneb kolmest loomast.
#Lisa selle listi lõppu kasutaja sisestatud lemmikloom.
#Väljasta see lemmikloomade list.
#Väljasta listi viimase elemendi viimane täht.

lemmikloom = input("Sisesta oma lemmikloom: ")

print("Lemmiklooma esimene täht:", lemmikloom[0])

animals = ["kass", "koer", "hobune"]

animals.append(lemmikloom)

print("Loomade list:", animals)

print("Viimase looma viimane täht:", animals[-1][-1])
