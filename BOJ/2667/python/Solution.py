import sys 
sys.setrecursionlimit(10**7)
IN = sys.stdin.readline
N = int(IN())

apart = list()
visited = [[0 for _ in range(N)] for _ in range(N)]

numOfAprt = list()  #단지 내 집 수
numOfCom = 0    # 단지 수

for i in range(N):
    apart.append(list())
    for j in IN().strip():
        apart[i].append(int(j))

cases = [(1,0),(0,1),(-1,0),(0,-1)] # DFS 이동할 때 경우의 수

def dfs(x, y) : 
    global count
    count += 1
    visited[y][x] = 1
    for xx, yy in cases:
        if 0<=xx+x<N and 0<=yy+y<N :
            if apart[y+yy][x+xx] == 1 and visited[y+yy][x+xx] != 1:
                dfs(x+xx, y+yy)

for i in range(N):
    for j in range(N):
        if apart[i][j] == 1 and visited[i][j] == 0:
            count = 0
            dfs(j,i)
            numOfAprt.append(count)
            numOfCom += 1

print(numOfCom)
numOfAprt.sort()
for i in numOfAprt:
    print(i)