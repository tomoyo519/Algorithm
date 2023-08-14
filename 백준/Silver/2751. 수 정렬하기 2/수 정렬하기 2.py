count = int(input())
arr = []

for i in range(0, count):
    number = int(input())
    arr.append(number)
    
arr.sort()
for j in arr:
    print(j)