import sys
input = sys.stdin.readline

number = int(input())
tree= {}

for n in range(number):
    root, left, right = input().strip().split()
    tree[root] = [left,right]
# print('tree', tree)

# 전위순회 : 루트/ ->왼쪽자식 ->왼쪽자식의 자식이 있다면 왼쪽자식 -> 없으면 오른쪽 자식, 루트의 오른쪽 자식 -> 그 자식이 자식이 있다면 왼쪽자식 -> 오른쪽 자식 -> 그 자식의 
def preorder(root):
    if(root != '.'):
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])
        

# 중위순회 : 왼쪽 자식 ->밑에서부터 루트까지 올라가고,  그게 끝이면 다음으로..넘어가기?
def inorder(root):
    if (root != '.'):
        inorder(tree[root][0])
        print(root , end='')
        inorder(tree[root][1])
        
# 후위순회 : 왼쪽에서부터 오른쪽으로 depths 낮은 순서대로 올라가기
def postorder(root):
    if(root !='.'):
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')
preorder('A')
print('')
inorder('A')
print('')
postorder('A')