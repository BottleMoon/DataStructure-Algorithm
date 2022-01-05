import sys
IN = sys.stdin.readline

def preorder(start):                    #전위 순회
    left, right = tree[start]
    print(start,end='')                 #print먼저 
    if left != '.' : preorder(left)     #왼쪽 탐색 재귀
    if right != '.' : preorder(right)   #오른쪽 탐색 재귀


def inorder(start):                     #중위 순회
    left, right = tree[start]
    if left != '.' : inorder(left)      #왼쪽 탐색 재귀 먼저
    print(start,end='')                 #왼쪽 부터 print
    if right != '.' : inorder(right)    #오른쪽 탐색 재귀

def postorder(start):                   #후위 순회
    left, right = tree[start]
    if left != '.' : postorder(left)    #왼쪽 탐색 재귀 먼저
    if right != '.' : postorder(right)  #오른쪽 탐색 재귀
    print(start,end='')                 #print

tree = dict()
N = int(IN())
for _ in range(N):
    L = IN().split()
    tree[L[0]] = (L[1],L[2])
    
preorder('A')
print()
inorder('A')
print()
postorder('A')