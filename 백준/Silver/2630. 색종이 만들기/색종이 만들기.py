number = int(input())

total = [list(map(int, input().split())) for _ in range(number)]

result = []

def findColor(x,y,n ):
    color = total[x][y];
    for i in range(x,x+n):
        for j in range(y, y+n):
            if(color != total[i][j]):
                findColor(x,y, n//2)
                findColor(x+(n//2), y, n//2)
                findColor(x, (y+(n//2)), n//2)
                findColor( x+(n//2), y+(n//2), n//2)
                return;

    if(color == 0):
        result.append(color)
    else:
        result.append(1)

findColor(0,0,number)

print( result.count(0))
print( result.count(1))