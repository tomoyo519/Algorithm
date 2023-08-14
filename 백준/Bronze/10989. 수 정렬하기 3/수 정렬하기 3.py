import sys
count = int(sys.stdin.readline())

arr = [0 for i in range(10001)]
# list = [0 for i in range(n)] 이거랑 무슨 차이 ??

for i in range(count):
    number = int(sys.stdin.readline())
    arr[number] +=1
    
for j in range(10001):
    if(arr[j]>0):
        # 그냥 print(j)하면 시간초과 나는 이유 ???
        for k in range(arr[j]):
            print(j)