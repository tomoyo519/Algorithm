import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

arr = []
pre_list = []

def post_order(left, right, pre_list):
    if (left > right): # 항상 오른쪽이 더 커야함
        return
    root = pre_list[left]
    point = left +1 # 분기점 기준
    while point <= right :
        if (pre_list[point] > root ):
            break;
        point +=1
    post_order(left+1, point -1, pre_list)
    post_order(point, right, pre_list)
    
    print(root)
    
while True:
    try:
        node = int(input())
        pre_list.append(node)
    except:
        break;
post_order(0, len(pre_list) -1 , pre_list)