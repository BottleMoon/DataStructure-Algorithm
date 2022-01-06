import sys
IN = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(IN())

tree = dict()
result = dict()
for i in range(1,N+1):
    tree[i] = list()
    result[i] = 0

#노드간 연결 저장
for _ in range(N-1):
    m,n = map(int,(IN().split()))
    tree[m].append(n)
    tree[n].append(m)

#1부터 DFS로 탐색
def sol(root):
    for i in tree[root]:
        if result[i] == 0:
            result[i] = root
            sol(i)

sol(1)

for i in range(2,N+1):
    print(result[i])