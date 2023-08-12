up , down, meter = map(int, input().split())

day = up - down;
almost = meter - up;

countDay = 1;

if( almost % day != 0  ):
    countDay = (almost // day) +1;
    countDay +=  1
    
else:
    countDay = (almost // day) +1
    
print(countDay)