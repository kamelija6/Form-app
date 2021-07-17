# class Licnost:
#     def __init__(self, ime, god):
#         self.ime = ime
#         self.god = god
#         print('(Inicijaliziram Licnost: {0})'.format(self.ime))

#     def kazi(self):
#        print('Ime:"{0}" Godini:"{1}"'.format(self.ime,
# self.godini),end = " ")



# class Prof(Licnost):
#     def __init__(self, ime, god, plata):
#         self.plata = plata
#         print('(Inicijaliziram profesor: {0}  )'.format(self.ime))
#     def kazi(self):
#         Licnost.kazi(self)
#         print('Plata: "{0:d}"'.format(self.plata))



# class Student(Licnost):
#     def __init__(self, ime, god, index):
#         self.index = index
#         print('(Inicijaliziram Student: {0})'.format(self.ime))

#     def kazi(self):
#         Licnost.kazi(self)
#         print('Indeks: "{0:d}"'.format(self.indeks))


# p = Prof("Cveta bande ", 55, 1000)
# s = Student("Kamelija", 22, 102218)
# print()
# clenovi = [p, s]
# for clen in clenovi:
#     clen.kazi()
# print()



# for i in range(0,30,5):
#     print(i)

# for i in range(6,0,-1):
#     print(i)


# # for i in range(1,5):
# #     for j in range(1,5):
# #         print("{0:2}".format(i*j),end='')

# # print()



n =[0]*5
def vnes(n):
    for i in range(0,5):
        n[i] = int(input("vnesi broj : "))
    
def ispist(n):
    for i in range(0,5):
        print(n[i], end="")

def obratno(n):
    for i in range(4,-1,-1):
        print(n[i], end='')

def parni(n):
    for i in range(1,5,2):
        print(n[i],end='')

while(1):
    print(" izberi ")
    print("1.Vnes na podatoci")
    print("2.Ispis na podatoci")
    print("3.Ispis vo obraten redosled")
    print("4.Ispis na elementi na parna pozicija")
    print("5.Izlez")
    izber = int(input("Vensi izbor "))

#     if izber == 1:
        vnes(n)
    elif izber == 2:
        ispist(n)
    elif izber == 3:
        obratno(n)
    elif izber == 4:
        parni(n)
    else:
        break

