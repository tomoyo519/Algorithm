import sys

A,B,C = map(int, sys.stdin.readline().split())

def divide_andCouquer(a,b):
    if(b ==1):
        return a % C
   
    tmp = divide_andCouquer(a, b//2);
    if(b % 2 ==0):
        return tmp * tmp % C
    else:
        return tmp * tmp *  a % C
    
print(divide_andCouquer(A,B))