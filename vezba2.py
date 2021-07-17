# print("hello world")

# for i in range(3):
#     print("Hello World")

# txt = "#Ova e komentar"
# print(txt)

# x = 5
# y = 8
# print(x + y)

# jadenje = " ovosje"
# pari = 0

# if jadenje == "ovosje" or jadenje == "brza hrana" and pari > 2:
#     print("JAdenjeto e doneseno")
# else:
#     print("Jadenjeto ne e doneseno ")

# z = complex(1.11, 2.22)
# print(z)
# print(z.real)
# print(z.imag)

# miki = 'Ova e niza "zadaci"'
# print(miki)

# p =""" Prva linja
#    Kaj si be ti
#         So praves tuka """
# print(p)

# p = "ej zdr kako e "
# print(p[0:6])
# print(p[:6])

# a = 15
# b = 5.8

# print(float(b))
# print(int(a))
# print(complex(a))
# print(hex(a))
# print(oct(a))

# p = "Kaj si be peder"

# print(len(p))
# # c = title(p)
# print(p.title())
# print(p.lower())
# print(p.upper())
# print(p.capitalize())
# print(p.lstrip())
# print(p.rstrip())
# print(p.strip())

# X = 8

# if X > 5:
#     print("Uslovot e zadovolen")
# else:
#     print("Uslovot ne e zadovolen")
# x = 5
# if x == 1:
#     print("Uslovot e zadovolen")
# elif x == 5:
#     print("Uslovot e zadovolen")
# else:
#     print("Uslovot ne e zadovolen")

# x = 5
# while x < 10:
#     print("hello")
#     x = x + 1

# a = ["dog", "cat", "miki"]
# for x in a :
#     print(x, len(x))


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for x in a:
#     print(x)

# for i in range(15, 20):
#     print(i)

# n = 55
# prim = True

# for x in range(2, n):
#     if n % x == 0:
#         prim = False
# if prim == True:
#     print(f"brojot {n} e paren")
# else:
#     print(f"brojot {n} ne e paren")

# for n in range(2, 11):
#     prim = True
#     for x in range(2, n):
#         if n % x == 0:
#             prim = False
#     if prim == True:
#         print(f"brojot {n} e prost")
#     else:
#         print(f"brojot {n} ne e prost")

# for n in range(2, 11):
#     prim = True
#     for x in range(2, n):
#         if n % x == 0:
#             prim = False
#             break
#     if prim == True:
#         print(f"brojot {n} e prost")
#     else:
#         print(f"brojot {n} ne e prost")

# for num in range(2, 6):
#     if num % 2 == 0:
#         print(f"Brojot e paren: {num}" )
#         break
#     print(f"brojot nee paren: {num}")

# def povik():
#     print("hello")


# povik()

# def suma(x, y):
#     print(x + y)


# suma(15, 60)

# x = "Hello! "
# y = 55
# z = "M"

# print(x, y, z, sep='---')

# import math
# print(math.pi)

# lista = ["Miki", "Krstev", 23]
# lista.append("peder")
# lista.clear()

# for x in lista:
#     print(x)


# lista = [2, 3, 4, 5, 6]
# lista.sort()
# lista.reverse()
# print(lista)
# nova = [10, 15]
# print(nova)
# # nova = lista.copy()
# print(nova)
# print(lista.count(4))
# nova.extend(lista)
# print(lista.index(6))


# mnoz = {1, 5, 6, 2, 3, 4, 7, 8, 9}
# moz = {1, 5, 2, 7}

# print(mnoz ^ moz)
# unija |
#  pesek &, razlika -, komplement na presek ^

# recnik = {1 : "januari", 2 : "februari", 3:"Mart", 4:"April", 5:"Maj", 6:"juni", 7:"juli", 8:"Avgust", 9:"Septemvri", 10: "Oktomvri", 11:"Noemvri", 12:"dekemvri"}
# recnik.update({13: "Peder"})
# del recnik[13]
# print(len(recnik))
# print(recnik.values())keys()

# class Peson:
#     def Hello(self):
#         print("KAko si ?")


# Peson().Hello()

# class Pesron:
#     def __init__(self, ime):
#         self.ime = ime
#     def koz(self):
#         print("JAde mi se bole me meseto", self.ime)


# Pesron('Stanka').koz()

# class Person:
#     populacija = 0
#     def __init__(self, ime):
#         self.ime = ime
#         print(f'KAj si be peder {self.ime}')
#     def __del__(self):
#         print(f"Dobar li si  be {self.ime}")
#         Person.populacija -= 1
#         if Person.populacija == 0:
#             print(f"Bese posledne" .format(self.ime))


# Person

# god = 22
# ime = "Kamelija"
# print(f"{ime} imala {god} koga ja napisala knigata")

# ime = input(">")
# ime2 = input(">")

# if sorted(ime) == sorted(ime2):
#     print("Se anagrami  ")
# else:
#     print("ne se anagrami ")


# num = [2, 7, 15, 11]
# tar = 9
# sum = num[0] + num[1]
# if sum == tar:
#     print(f"1 i 2 broevite na pozicijata se vo suma na {sum} ")
#     print("[0, 1]")

# l = [2, 4, 3]
# l1 = [5, 6, 4]

# sum = 0 
# while l or l1 or sum:
#     l.reverse()
#     l1.reverse()


# print(sum)

# chars = "abcabcbb"


# num = ["1", "3"]
# num.insert(1, "2" )

# print(float(num[1]))


# num1 = [1, 2]
# num2 = [3, 4]

# sum = (num1[1] + num2[0]) / 2
# print(float(sum))

# x = [1, 2, 3]
# x.reverse()
# print(x[:2])

# def funkcija(a, b = 5, c = 10):
#     print('a = ', a, 'b = ', b, 'i c = ', c)

# funkcija(3, 4)
# funkcija(25, c = 25)
# funkcija(c = 50, a = 100)

# def total(i = 0, *broevi, **klucnizborovi):
#     broenje = i
#     for broj in broevi:
#         broenje += broj
#     for zbor in klucnizborovi:
#         broenje += klucnizborovi[zbor]
#     return broenje

# print(total(10, 1, 2, 3, zelencuk = 50, ovosje = 100))


# def sum(i = 5, *broj, ekstra_broj):
#     broi = i
#     for broevi in broj:
#         broi += broevi
#     broi += ekstra_broj
#     print(broi)

# sum(10, 1, 2, 3, ekstra_broj=50)


# a = int(input("Vnesi broj: "))
# b = bin(a)
# print(id(a))

# for i in range(0,6,2):
#     print(i)

# for i in range(6,0,-1):
#     print(i)

# for red in range(1,11):
#     for kolona in range(1,11):
#         print("{0:5}".format(red*kolona), end="")
# print()

# def praren(n):
#     if n % 2 == 0:
#         print("paren e ")
#     else:
#         print("brojot ne e paren")
#     return
# praren(5)



# def zbir():
#     n = int(input("venesi broj: "))
#     m = int(input("Vnesi dr broj: "))
#     sum = n + m
#     return sum

# print(zbir())

# def vnes(niza):
#     for i in range(0,5):
#         niza[i]=int(input("vnesi broj "))

# def ispis(niza):
#     for i in range(0,5):
#         print(niza[i], end='')

# niza = [0] * 5
# vnes(niza)
# ispis(niza)


# niza = [0]*5
# def funk(niza):
#     for i in range(0,5):
#         niza[i]=int(input("Vnesete broj: "))
# def ispis(niza):
#     for i in range(0,5):
#         print(niza[i],end='')
# def obratno(niza):
#     for i in range(4,-1,-1):
#         print(niza[i],end='')
# def parni(niza):
#     for i in range(1,5,2):
#         print(niza[i],end='')


# i=0
# while 1:
#     print("Izberete")
#     print("1.Vnes na podatoci")
#     print("2.Ispis na podatoci")
#     print("3.Ispis vo obraten redosled")
#     print("4.Ispis na elementi na parna pozicija")
#     print("5.Izlez")
#     izbor=int(input("Vas izbor"))
#     if izbor==1:
#         funk(niza)
#     elif izbor==2:
#         ispis(niza)
#     elif izbor==3:
#         obratno(niza)
#     elif izbor==4:
#      parni(niza)
#     elif izbor==5:
#         break    
