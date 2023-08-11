num = int(input())

for i in range(num):
    result = ''
    a, b = map(str, input().split())
    for j in list(b):
        result += j*int(a)
    print(result)
