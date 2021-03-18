plik = open("kontakty.txt","a")

if plik.writable():

    plik.write(input("Imie: ") + "\n")
    plik.write(input("Nazwisko: ") + "\n")
    plik.write(input("Narodowość: ") + "\n")
    plik.write(input("Telefon: ") + "\n")
    plik.write(input("<==============================> ( ENTER --> ZATWIERDZ )") + "\n")

plik.close()


plik = open("kontakty.txt","r")

if plik.readable():

    print("Dane: ")
    linia = plik.read()
    print(linia)