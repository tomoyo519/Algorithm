# 3장을 뽑아서 만들 수 있는 합의 경우 중에서, 만들어야 되는 수랑 가장 차이가 작은것 (음수눈 안됌)

import itertools;

cardNum, goalNum = map(int,input().split())
cardList = []

cardList = (input().split())

gap = []
nPr = list(itertools.permutations(cardList, 3))
for k in nPr:
    total = 0;
    total = int(k[0]) + int(k[1]) + int(k[2]);

    if(goalNum - total >= 0):
        gap.append(total)

print(max(gap))