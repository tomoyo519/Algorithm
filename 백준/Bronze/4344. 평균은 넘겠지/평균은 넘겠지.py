a = input()

for i in range(1, int(a)+1):
    arr = (input().split())
    sum = 0
    for j in arr[1:]:
        sum += int(j)
    reverage = sum / int(arr[0])
    overReverage = 0;
    for k in arr[1:]:
        if(int(k) > reverage):
            overReverage += 1;
    percent = round(overReverage / int(arr[0])* 100, 3)
    print(str(percent)+"%" )