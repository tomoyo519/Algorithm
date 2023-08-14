import random;

arr = []
flag = True;
result = []

for i in range(0,9):
        nanjang = int(input())
        arr.append(nanjang)
while(flag):
    total = 0;
    checkNanjang = random.sample(arr, 7);
    for j in checkNanjang:
        total += j;
    if(total == 100):
        result = checkNanjang
        flag = False;
        
result.sort()
for k in result:
    print(k)