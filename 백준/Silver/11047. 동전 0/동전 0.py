import sys
input = sys.stdin.readline

coinNumber, total = map(int,input().split())

coinArr = [int(input()) for _ in range(coinNumber)]

coinArr.sort(reverse=True)
count = 0;

for coin in coinArr:
    while(coin <= total):
        total -=coin;
        count+=1
        
    
print(count)