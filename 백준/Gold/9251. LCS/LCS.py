import sys
input = sys.stdin.readline
# 이거 어케쪼ㅓ개 한글자를 찾을때? 
string1 = str(input().rstrip().upper())
string2 = str(input().rstrip().upper())

len1 = len(string1)
len2 = len(string2)

cache = [0] * len2;
for i in range(len1):
    count = 0;
    for j in range(len2):
        if count < cache[j]:
            count = cache[j]
        elif string1[i] == string2[j]:
            cache[j] = count+1;

print(max(cache))