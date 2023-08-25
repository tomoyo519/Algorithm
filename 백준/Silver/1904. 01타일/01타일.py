import sys
input = sys.stdin.readline

def tile(num):
    cached = [0 for _ in range(num+2)]
    cached[0] =0
    cached[1] =1
    
    for i in range(2, num+1):
        cached[i] = (cached[i-2] + cached[i-1])  % 15746
    return cached[num]

N = int(input())
print(tile(N+1) )