# 이분탐색 left right 
# 일단 처음과 마지막에는 설치
# 공유기의 거리 계산 = 1 ,4, 9 = 거리는 3 
# 공유기를 설치할 거리를 이분탐색으로 결정하기
import sys
input = sys.stdin.readline
N, C =  map(int,input().split())
house = list(int(input().rstrip()) for _ in range(N));
# 집들의 거리는 일직선에 위치함.

house.sort();

start, end = 1, house[N-1] - house[0];
# 집사이의 최소거리, 최대거리

result = 0;

if(C==2): # 집이 두개라면, 무조건 처음집과 마지막집 사이의 거리
    print(house[N-1] - house[0]); 
else:
    while(start<end):
        mid = (start + end ) // 2; # 최소거리 + 최대거리 / 2
        count = 1; # 거리 추가
        ts = house[0]; #공유기가 마지막으로 설치된 곳
        
        for i in range(N):
            if house[i] - ts >=mid:
                count+=1 #공유기설치
                ts = house[i] #마지막으로 공유기설치한곳 업데이트
        if count >= C: #공유기의 간격 좁히기
            result = mid    
            start = mid +1
        elif count < C:
            end = mid # 공유기의 간격을 줄이기
    print(result)
