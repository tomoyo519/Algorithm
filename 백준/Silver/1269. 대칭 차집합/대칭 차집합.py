import sys
input = sys.stdin.readline

lengthA, lengthB = map(int, input().split());
arrA = set(list(map(int, input().split())));
arrB = set(list(map(int, input().split())));

numA = (arrA - arrB);
numB = (arrB - arrA);

print(len(numA) + len(numB))