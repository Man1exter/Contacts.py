
wybor = int(input(" --- ZAPIS[1] --- CZY --- ODCZYT[2] --- " + "\n"))

if wybor == 1:
 plik = open("kontakty.txt", "a")

 if plik.writable():

    plik.write(input("Imie:  " + "\n"))
    plik.write(input("Nazwisko:  " + "\n"))
    plik.write(input("Narodowość:  " + "\n"))

    telefon = input("Telefon: ") #zmienna...

    if telefon != int:
        print("Wprowadziles zle dane, popraw je")
        telefon = input("Telefon:  ")
        plik.write(telefon)
    else:
        plik.write(telefon)

    plik.write(input("( ENTER --> ZATWIERDZ )") + "\n")

    plik.close()

else:

 plik = open("kontakty.txt", "r")

 if plik.readable():

    print("Dane: ")
    linia = plik.read() 
    print(linia)