import sys
input = sys.stdin.readline

count = input()
s = sorted(list(map(int, input().split())))

check_count = input()
m = (list(map(int, input().split())))

result = []

def search(target):
    l, r = 0, len(s)-1;

    while l<=r:
        mid = (l+r) // 2
        if s[mid] == target:
            return True
        elif s[mid] < target:
            l = mid+1
        elif target<s[mid]:
            r = mid -1
    return False

for i in m:
    if search(i) :
        result.append("1")
    else:
        result.append("0")
#     if( i in s ):
#         result.append("1")
#     else:
#         result.append("0")

print(' '.join(result));
