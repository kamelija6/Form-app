# varArgs

# def fkupno(i = 0, *br, **zbor ):
#     broj = i
#     for bro in br:
#         broj += bro
#     for zb in zbor:
#         broj += zbor[zb]
#     return broj

# print(fkupno(15, 6, 5, 8, ovosje = 70, piperki = 17))

# def fkupno(i = 5, *br, plus_br):
#     broj = i
#     for broevi in br:
#         broj += broevi
#     broj += plus_br
#     print(broj)

# fkupno(150,5,1, plus_br = 6)  

# for i in range(1,5):
#     for j in range(1, 5):
#         print("{0:5}".format(i*j), end ='')

# print()

# n = int(input("Vnesi broevi :"))

# def paren():
#     if n%2 ==0:
#         print("br e paren")
#     else:
#         print("br ne e paren ")
#     return

# paren()

# def zbri():
#     m = int(input("vensi br: "))
#     n = int(input("vensi dr br: "))
#     k = m + n
#     return k


# print(zbri())

# def vens(niza):
#     for i in range(0, 5):
#         niza[i] = int(input("vnesi br: "))

# def ispis(niza):
#     for i in range(0, 5):
#         print(niza[i], end='')

# niza = [0] * 5
# vens(niza)
# ispis(niza)

# def vnes(niza):
#     for i in range(0,5):
#         niza[i] = int(input("vnesi br : "))
    
# def ispis(niza):
#     for i in range(0,5):
#         print(niza[i], end='')

# def obratno(niza):
#     for i in range(4,-1,-1):
#         print(niza[i], end='')

# def parni(niza):
#     for i in range(1,5,2):
#         print(niza[i], end='')

# i = 0
# niza=[0]*5
# while(1):
#     print("izveri sam: ")
#     print("1.Vnes na podatoci: ")
#     print("2.Ispis na podatoci: ")
#     print("3.Ispis vo obraten redosled: ")
#     print("4.Ispis na el na prani ppozicii: ")
#     print("5.Kraj ")
    
#     izbor = int(input("Vnesi izbor: "))
#     if izbor == 1:
#         vnes(niza)
#     elif izbor == 2:
#         ispis(niza)
#     elif izbor == 3:
#         obratno(niza)
#     elif izbor == 4:
#         parni(niza)
#     elif izbor == 5:
#         break


# niza = [1,2,3,4,5,6,7,8,9,10]
# niza1 =[0]*5
# j=0
# for i in range(0,10):
#     if niza[i] % 2 ==0:
#         niza1[j]=niza[i]
#         j+=1
# print("Ispis na prvata niza")
# for i in range(0,10):
#     print(niza[i], end='')
# print()
# print("Ispis na vtorata niza")
# for i in range(0, j):
#     print(niza1[i], end='')
# print()


# n = [5, 8, 15, 2, 6, 7, 0, 1, 51, 78]
# min=max=n[0]
# for i in range(0,10):
#     if min > n[i]:
#         min = n[i]
#     elif max < n[i]:
#         max=n[i]
#     else:
#         print("ti si peder")

# print("Naj golemio br e : " , max)
# print("Naj malio br e : " ,min)

# n = [5, 8, 15, 2, 6, 7, 0, 1, 51, 78]
# for i in range(len(n)-1,1,-1):
#     for j in range(0, i, 1):
#         if n[j]>n[j+1]:
#             temp = n[j]
#             n[j] = n[j+1]
#             n[j+1] =temp
# print(n)

# n = [5, 8, 15, 2, 6, 7, 0, 1, 51, 78]
# for i in range(len(n)):
#     temp = n[i]
#     j = i
#     while j>0 and n[j-1]>=temp:
#         n[j] = n[j-1]
#         j=j-1
#     n[j]=temp
# print(n)


# n = [5, 8, 15, 2, 6, 7, 0, 1, 51, 78]

# def swap(i,j):
#     temp = n[i]
#     n[i] = n[j]
#     n[j] = temp
# for out in range(len(n)-1):
#     min =out
#     for i in range(out + 1, len(n)):
#         if n[i]<n[min]:
#             min = i
#     swap(out, min)
# print(n)

# a =[]
# for i in range(3):
#     a.append([])
#     for j in range(3):
#         a[i].append(i+j)
# print(a)

# n = int(input("Vnesi broj na redovi: "))
# m = int(input("Vnesi broj na koloni: "))
# a=[]
# for i in range(n):
#     b = []
#     for j in range(m):
#         b.append(input("Vnesenite el se [{0},{1}]".format(i,j)))
#     a.append(b)
# print(a)

# a = (input("Vnesi ime "))

# print(f"Tvoeto ime e {a}")


# n = int(input("Vnesi broj na redovi: "))
# m = int(input("Vnesi broj na koloni: "))
# a=[]

# for i in range(n):
#     b=[]
#     for j in range(m):
#         b.append(int(input(f"Vnesenite el {i, j}")))
#     a.append(b)
# print(a)


# a= []
# for i in range(3):
#     a.append([])
#     for j in range(3):
#         a[i].append(i+j)
# print(a)
# b = []
# for i in range(3):
#     b.append([])
#     for j in range(3):
#         b[i].append(i+j)
# print(b)
# c = a + b
# print(c)


# m =[]
# m.append([1,2,3])
# m.append([4,5,6])
# m.append([7,8,9])
# print ("Ispis na celata lista so podlistite")
# print (m)
# print ("Ispis red po red")
# for red in m:
#     print(red)
# print ("Ispis na site elementi")
# for red in m:
#     for el in red:
#         print(el, end='')
# print()

# class Miki:
#     def setPeder(self, nes):
#         self.nes = nes
#     def getPeder(self):
#         print(self.nes)

# p = Miki()
# p.setPeder("MIKI pederoooo")
# p.getPeder()

# class Car:
#     def __init__(self, model, boja):
#         self.model = model
#         self.boja = boja
#     def pecat(self):
#         print('Kolata e so: ',self.boja, self.model)
#     def novab(self,novaboja):
#         self.boja =novaboja

# car1 = Car("Mercedes", "Mat Crna")
# car1.pecat()
# car2=Car("BMW", "Bela")
# car2.pecat()

# class Basket:
#     def __init__(self, owner =''):
#         self.owner = owner
#         self.content = []
#     def add(self, item, quantity):
#         self.content.append((item, quantity))
#     def add_multi(self, aList):
#         for item, quantity in aList:
#             self.add(item,quantity)
#     def remove_multi(self, aList):
#         for item in aList:
#             self.remove_multi(item)
#     def sum(self):
#         tot = 0
#         for item, quantity in self.content:
#             tot+=quantity*item.price
#         return tot


# class Item:
#     def __init__(self, name, price):
#         self.name =name
#         self.price =price


# class Ebasket(Basket):
#     def remove(self, item):
#         for art in reversed(self.content):
#             if art[0] == item:
#                 self.content.remove(art)


# b = Ebasket()
# banana= Item("banan", 1.20)
# b.add(banana,20)
# b.add(Item("Melko ",1.40),12)
# print(b.sum())
# b.remove_multi([banana])
# print(b.sum())


# class bool(int):
#     def __str__(self):
#         if self == 0:
#             return "False"
#         elif self == 1:
#             return "True"
#         else:
#             return super().__str__(self)
#     __repr__ = __str__

# true = bool(0)
# false = bool(1)
# print(false)

# def fibo(n):
#     a = b = 1
#     for i in range(n):
#          a, b = b, a+b
#     return a
# print(fibo(6))


# s = [("Ana", 63),("Celi", 22),("Miki", 23)]
# def vrati(c):
#     return c[1]
# # s.sort(key=vrati)
# s.sort(key=lambda c: c[1])
# print(s)

# def cmp(a, b):
#     if a < b:
#         return -1
#     elif a > b:
#         return 1
#     else:
#         return 0
    
# print(cmp(5,8))

# def min(s):
#     mins = s[0]
#     for e in s:
#         if e < mins:
#             mins = e
#     return mins
# s = [ 5, 8, 2, 3, 1,5, 1]
# print(min(s))

# def min(s):
#     mm, mins = s[0],0
#     for e in range(len(s)):
#         if s[e] < mm:
#             mm, mins = s[e], e
#     return mins, mm
# s = [ 5, 8, 2, 3, 1,5, 1]
# print(min(s))