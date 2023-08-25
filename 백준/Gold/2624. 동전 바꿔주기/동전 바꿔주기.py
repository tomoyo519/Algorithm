# 교환가능 가짓수에 대한 점화식
import sys
input = sys.stdin.readline

total = int(input())
line = int(input())

solutions = [ ]
for i in range(line):
    solutions.append(list(map( int,input().split())))

# solutions.sort(key=lambda x:x[0])
# dp[number] += dp[]
dp = [0] * (total +1)
dp[0] = 1
for coin,count in solutions:
    for i in range(total, 0, -1):
        for j in range(1, count+1):
            if(i>=(coin * j)):
                dp[i] += dp[i - (coin * j)]
print(dp[total])