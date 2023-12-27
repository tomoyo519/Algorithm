from collections import deque

while True:
    nums = deque(map(int, input().split()))
    k = nums.popleft()
    if k == 0:
        break

    s = []

    def dfs():
        if len(s) == 6:
            print(' '.join(map(str,s)))
            return

        for i in sorted(nums):
            if i not in s:
                if s:
                    if s[-1] > i:
                        continue
                s.append(i)
                dfs()
                s.pop()

    dfs()
    print()