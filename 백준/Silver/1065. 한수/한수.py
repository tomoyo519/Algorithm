number = int(input())
count = 0;
for i in range(1, number+1):
    arr = list((str(i)))
    if(len(arr) == 1 or len(arr) ==2):
        count+=1
    else:
        for j in range(0, int(len(arr))-2 ): 
            gap = int(arr[1]) - int(arr[0]); 

            if( int(arr[int(j) + 2]) - int(arr[int(j) + 1]) == gap):

                count+=1;
print(count)