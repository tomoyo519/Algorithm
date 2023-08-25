import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    
    dp = [0] * (M+1)
    dp[0] =1
   
    for coin in coins:
        for money in range(M, 0, -1):

            for i in range(1, 10001):
                if(money >= (i * coin)):
                    dp[money] += dp[money - (i*coin)]

    print(dp[M])