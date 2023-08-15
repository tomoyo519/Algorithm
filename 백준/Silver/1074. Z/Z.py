n,r,c = map(int, input().split())
# 전역변수는 global 로 꼭 선언

answer = 0;
def rec(startX, startY, length):
    global answer;
    if(startX ==c and startY ==r):
        print(answer)
        exit();
    if(startX <= c and startX+length > c and startY <= r and startY+ length > r):
        
        rec(startX, startY, length//2)
        rec(startX + length //2, startY , length //2 )
        rec(startX, startY + length//2 , length //2)
        rec(startX+length //2, startY+length //2, length//2)
    else:
        answer +=  (length * length)
    
rec(0,0,2**n);
