n= int(input())
num = n
count = 0;

while True:
    a = num // 10
    b = num % 10
    c = (a + b) % 10 
    newNum = ( 10 * b) + c
    count += 1
    if(newNum == n):
        break;
    else:
        num = newNum

print(count)
