#Kirjuta programm, mis küsib kasutajalt nime, tervitab teda nimepidi, küsib 
#kasutajalt elukoha, kui elukoht on Saaremaa, siis väljastab mingi kommentaari, 
#küsib kasutajalt vanuse, kui vanus on väiksem kui 18, siis ütleb, et kasutaja 
#on liiga noor, et autot juhtida, kui vanus on 18, siis õnnitleb täisealiseks 
#saamise puhul, kui kasutaja on vanem kui 18, siis ütleb, et kasutaja võib 
#autot juhtida. (sõne - string)

name = input("Sisesta oma nimi: ")
print("Tere, " + name + "!")

location = input("Sisesta oma elukoht: ")
if location.lower() == "saaremaa":
    print("Saaremaa on ilus koht!")

age = int(input("Sisesta oma vanus: "))
if age < 18:
    print("Oled liiga noor, et autot juhtida.")
elif age == 18:
    print("Palju õnne täisealiseks saamise puhul!")
else:
    print("Võid autot juhtida.")
