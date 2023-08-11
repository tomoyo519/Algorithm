a = input()

for i in range(0, int(a)):
    result = 0;
    count = 0;
    idx = 0;
    arr = list(input())
    for j in arr:
        if(j =='O'):
            count +=1
            idx +=1
            result += count;
        elif(j == 'X'):        
            count = 0;
            idx +=1
    print(result);