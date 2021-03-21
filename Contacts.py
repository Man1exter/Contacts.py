
print("\U0001F917" + "<TWOJ OSOBISTY DZIENNIK KONTATKOW>" + "\U0001F917")
wybor = int(input(" --- ZAPIS[1] --- CZY --- ODCZYT[2] --- CHOINKA[3] --- TUPLEINFO[4] ---" + "\n"))

if wybor == 1:
 plik = open("kontakty.txt", "a")

 if plik.writable():

    plik.write(input("Imie:  " + "\n"))
    plik.write(input("Nazwisko:  " + "\n"))
    plik.write(input("Narodowość:  " + "\n"))
    plik.write(input("Wiek:  " + "\n"))
    plik.write(input("Zawod wykonywany:  " + "\n"))

    telefon = input("Telefon: ") #zmienna...
    wiek = input("Wiek: ") #zmienna...

    if telefon != int:
        print("Wprowadziles zle dane, popraw je")
        telefon = input("Telefon:  ")
        plik.write(telefon)
    else:
        plik.write(telefon)

    if wiek != int:
        print("Wprowadziles zle dane, popraw je")
        wiek = input("Telefon:  ")
        plik.write(wiek)
    else:
        plik.write(wiek)

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

elif wybor == 4:
    
    krotka = (5,10,15,20,25,30,35,40,45)

    print(krotka[0])
    print(krotka[6])

else:

 plik = open("kontakty.txt", "r")

 if plik.readable():

    print("Dane Wszystkich Zapisanych: ")
    liniaPliku = plik.read() 
    print(liniaPliku)