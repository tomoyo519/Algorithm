number = int(input())
arr = []
def move(N, start, end):
    sentence = start + " " + end
    arr.append(sentence)
    
    
def hanoi(N, start, end, sub):
    if(N==1):
        move("1", str(start), str(end));
        return;
    else:
        hanoi(N-1, start, sub, end);
        # hanoi(1, start, end)
        move(str(N), str(start),str(end))
        hanoi(N-1, sub, end,start)

if(number <=20):            
    hanoi(number, "1","3","2")
    print(len(arr))

    for i in arr:
        print(i)
else:
    print( 2** number -1)
    


