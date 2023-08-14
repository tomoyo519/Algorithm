number = int(input())
arr = []
for i in range(0, number):    
        word = input()
        arr.append(word)

arr = list(set(arr))
arr.sort()
arr.sort(key =lambda x:len(x))
for k in arr:
    print(k)