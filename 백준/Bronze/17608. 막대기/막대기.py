import sys
input = sys.stdin.readline

number = int(input())

stickArr = []
for i in range(number):
    stickArr.append(int(input()))

currentMax = stickArr[-1]
count = 1
for j in range(number-1, -1, -1):  
    if(int(stickArr[j]) > currentMax):
       
        currentMax = int(stickArr[j])
        count += 1;

print(count)