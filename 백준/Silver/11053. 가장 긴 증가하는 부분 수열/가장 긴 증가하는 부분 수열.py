import sys
input = sys.stdin.readline

number = int(input())
arr = list(map(int,input().split()))

dp = [1] * (number +1 )

for i in range(1, number):
    for j in range(i):
        if( arr[i] > arr[j]):
            dp[i] = max(dp[i], dp[j]+1)
            
print(max(dp))