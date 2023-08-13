import itertools

num = int(input()) # 4 장의 카드중에서
card = int(input()) # 2 장을 골라서 숫자 조합을 만든다.
# 조합할 수 있는 숫자를 모두 배열에 넣은 다음 중복제거하기
cardArr = []
for i in range(0, num):
    
    cardArr.append(input())

nPr = itertools.permutations(cardArr, card)
result = []
nPr = list(nPr)

for j in range(0, len(list(nPr))):
    tmp = ""
    for i in range(0, card):
        tmp +=((list(nPr)[j][i]))
        
    result.append(tmp);
result = set(result)

print(len(result))
