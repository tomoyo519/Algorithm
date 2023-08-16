import sys
input = sys.stdin.readline
global hunter, animal, ans, L
hunter = []
animal = []
ans = 0
M, N, L = map(int, input().split())
hunter = list(map(int, input().split()))
hunter.sort()
animal = [list(map(int, input().split())) for i in range(N)]
def search(left, right, x, y):
    global ans, hunter, animal, L
    if left > right:
        return
    mid = (left + right) // 2
    if abs(hunter[mid] - x) + y <= L:
        ans += 1
        return
    if x < hunter[mid]:
        search(left, mid - 1, x, y)
    else:
        search(mid + 1, right, x, y)
for i in animal:
    search(0, M - 1, i[0], i[1])
print(ans)