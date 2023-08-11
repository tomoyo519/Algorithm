a, b ,c ,d = map(int, input().split())
smallest = a
x = (c - a)
y = (d - b)
for i in [b,c,d, x, y]:
    if(smallest > i):
        smallest = i


print(smallest)