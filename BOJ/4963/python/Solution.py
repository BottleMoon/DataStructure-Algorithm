import sys
from collections import deque

IN = sys.stdin.readline

dx, dy = [0,0,1,1,1,-1,-1,-1],[1,-1,1,0,-1,1,0,-1]

def sol() :
    N, M = map(int,IN().split())

    if N == M == 0 : return -1 # 0 0 나오면 -1 리턴

    graph = [[i for i in list(map(int,IN().split()))] for _ in range(M)]
    visited = [[0 for _ in range(N)] for _ in range(M)]

    numberOfLand = 0

    for h in range(M):
        for w in range(N):
            if visited[h][w] == 0 and graph[h][w] == 1 :     #발견 못한 섬이있으면
                numberOfLand += 1       #섬 개수 +1
                bfs(graph, visited, w, h)     #섬 정찰해서 방문기록 남김
    print(numberOfLand)


def bfs(graph, visited, x,y) :      # bfs 이용한 섬 탐색 함수
    queue = deque([(x,y)])
    visited[y][x] = 1 

    while(queue):
        x, y = queue.popleft()

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < len(visited[0]) and 0 <= ny <len(visited):

                if graph[ny][nx] == 1 and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    queue.append((nx,ny))
    return


while True :
    if(sol() == -1) : break