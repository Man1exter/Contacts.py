
print("<TWOJ OSOBISTY DZIENNIK KONTATKOW>")
wybor = int(input(" --- ZAPIS[1] --- CZY --- ODCZYT[2] --- CHOINKA[3]" + "\n"))

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

elif wybor == 3:

    print("CHOINKA NA ROZLUZNIONE DNI :>")

    size = 7
    m = ( 2 * size ) - 2

    for ele in range(0,size):
       for ele2 in range(0,m):
           print(end = "" + "\n")
       m = m - 1
       for ele2 in range(0,ele + 1):
          print("* ",end = " ")
    print(" ")

else:

 plik = open("kontakty.txt", "r")

 if plik.readable():

    print("Dane Wszystkich Zapisanych: ")
    liniaPliku = plik.read() 
    print(liniaPliku)