import sys
input = sys.stdin.readline
number = int(input())

def fibo(num):
    arr = [0 for _ in range(number+2)]
    arr[0] = 0
    arr[1] = 1
   
    for i in range(2, num+1):
       arr[i] = arr[i-2] + arr[i-1]
    return arr[num]
    
print(fibo(number))