up , down, meter = map(int, input().split())

day = up - down;
almost = meter - up;

countDay = 0;

if( almost % day != 0  ):
    countDay = (almost // day) +2
    
else:
    countDay = (almost // day) +1
    
print(countDay)