import sys
count = int(sys.stdin.readline())

arr = [0] * 10001

for i in range(count):
    number = int(sys.stdin.readline())
    arr[number] +=1
    
for j in range(10001):
    if(arr[j]>0):
        for k in range(arr[j]):
            print(j)