import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins= []
for _ in range(N):
    coins.append(int(input().rstrip()))
coins.sort()
dp= [10001] * (K+1)
dp[0] = 0

for i in range(1, K+1):
    for coin in coins:
        if i-coin < 0:
            break;
        else:
            dp[i] = min(dp[i - coin]+1, dp[i])
if( dp[K] ==10001):
    print(-1)
else:
    print(dp[K])