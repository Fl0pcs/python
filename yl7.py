#Kirjuta programm, mis ütleb, kas kasutaja poolt etteantud täisarv 
# on paarisarv või mitte. (paarisarvu mõiste - odd/even)

number = int(input("number: "))
if number % 2 == 0:
    print("Number on paaris.")
else:   
     print("Number on paaritu.")