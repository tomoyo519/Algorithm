import sys
import math

check = [True for i in range(int(10000)+1)]
for i in range(2, int(math.sqrt(int(10000)))+1):
    if check[i] == True:
        j=2
        while i*j <=int(10000):
            check[i*j] = False
            j+=1
result = []
for i in range(2, int(10000)+1):
    if (check[i]):
        result.append(i)

number= int(input())

for _ in range(number):
    num = int(input())
    a = num //2
    b = num //2
    while a > 0:
       if a in result and b in result:
            print(a ,b)
            break;
       else:
           a -=1
           b +=1