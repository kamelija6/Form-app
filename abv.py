# m = 5 
# n = 9
# k = m + n
# print(k)

# a  = 5
# b = 7

# if a>b:
#     print(a)
# elif a<b:
#     print(b)
# else:
#     print("nis ne praveme")

# def zadaca(n):
#     if n < 0:
#         return 0
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         f = 1
#         while(n>1):
#             f*=n
#             n-=1
#         return f

# n = 7
# print(n, zadaca(n))
import math

# m = int(input("br 1 : " ))
# n = int(input("br 2 : " ))
# l = int(input("br 3 : " ))

# k = (m * n * l)/100 

# print(k)

# def sum(p, r, t):
#     a = p*(pow((1+r/100), t))
#     k = a - p
#     print(k)

# sum(15, 20, 4)

# def power(r):
#     pi = 3.14
#     return pi*(r*r)

# print(power(4))

# s = 5
# e = 10
# for i in range(s, e+1):
#     if i > 1:
#         for j in range(2, i):
#             if i % j== 0: 
#                 break
#         else:
#              print(i)
# def fibo(n):
#     if n<0:
#         print("ne e fibonaci br")
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)

# print(fibo(9))

# def sum(arr):
#     suma = 0
#     for i in arr:
#         suma += i
#     return suma

# arr = []
# arr = [12, 3, 4, 15]
# n = len(arr)
# ans = sum(arr)
# print(ans)

# def max(arr, n):
#     max = arr[0]
#     for i in range(1, n):
#         if arr[i]>max:
#             max =arr[i]
#     return max

# arr = [12, 15, 13, 88, 10]
# n = len(arr)
# ans = max(arr, n)
# print(ans)


# def smena(arr, n, d):
#     temp = []
#     i = 0
#     while i < d:
#         temp.append(arr[i])
#         i += 1
#     i = 0
#     while d < n:
#         arr[i] = arr[d]
#         i = i + 1 
#         d = d + 1
#     arr[:] = arr[: i] + temp
#     return arr

# arr = [1,2,3,4,5,6,7]
# print(smena(arr, len(arr), 2))


# def smena(lista):
#     size = len(lista)

#     temp = lista[0]
#     lista[0] = lista[size - 1]
#     lista[size - 1] = temp

#     return lista

# lista = [ 12, 35, 8, 65, 25]
# print(smena(lista))


# def smena(list, post1, post2):
#     list[post1], list[post2] = list[post2], list[post1]
#     return list 

# list = [25, 56, 43]
# post1, post2 = 1, 3
# print(len(list))


# def reve(list):
#    list.reverse()
#    return list

# list = [1,5,6,7,2,9,3,2]
# print(reve(list))


# def mnozenje(l):
#     r = 1
#     for i in l:
#         r *= i
#     return r
# list = [1,5,6,7,2,9,3,2]
# print(mnozenje(list))

# l = [10, 20, 4,45, 99]
# l.sort()
# print("najmal el e : ", *l[:1])
# print("najgolem el e : ", l[-1])

# list1 = [11, -21, 0, 45, 66, -93]
# for num in list1:
#     if num < 0:
#         print(num, end="") 

# X = [[1,2,3],
#     [4 ,5,6],
#     [7 ,8,9]]

# def zbor(s):
#     s = s.split(' ')
#     for i in s:
#         if len(i) % 2 == 0:
#             print(i)
# s ="Kaj si be tii"
# zbor(s)

# Y = [[9,8,7],
#     [6,5,4],
#     [3,2,1]]

# rez = [[0, 0, 0],
#         [0, 0, 0],
#         [0, 0, 0]]

# for i in range(len(X)):
#     for j in range(len(X[0])):
#         rez[i][j] = X[i][j] + Y[i][j]

# for r in rez:
#     print(r)

# n = input("vnesi zbor: ")

# def pp(n):
#     if n == n[::-1]:
#         print("E polondrom :P ")
#     else:
#         print("Ne  e polindorm :(")

# pp(n)


# def rev(s):
#     w = s.split(' ')
#     snet = " ".join(reversed(w))
#     return snet

# if __name__ == "__main__":
#     input = "Zdravo so praves?"
#     print(rev(input))

# import re

# def run(string):
#     regx = re.compile('[@_!#$%^&*()<>?/\|}{~:}]')
#     if regx.search(string) == None:
#         print("Tocno")
#     else:
#         print("Ne tocno")
    
# if __name__ == '__main__':
#     string = "Kako& e& So ^si% praves"
#     run(string)
