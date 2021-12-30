import sys
from collections import deque
IN = sys.stdin.readline

N, M = map(int,IN().split())
g = [0 for _ in range(N)]

dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]

for i in range(N):
    g[i] = [int(i) for i in list(IN())[:M]]
 
visited = [[[0,0] for _ in range(M)] for _ in range(N)]




def sol(g, visited):
    queue = deque([(0,0)])
    visited[0][0][0] = 1
    while(queue):
        x, y = queue.popleft()
        
        if x == M-1 and y == N-1:   #목적지 도착하면 길이 반환
            return (visited[y][x][0]) 
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= ny < N and 0 <= nx < M:

                if visited[y][x][1] == 0 and g[ny][nx] == 1:    #벽 안뚫었는데 벽 만났을 때
                    visited[ny][nx][0] = visited[y][x][0] +1
                    visited[ny][nx][1] = 1
                    queue.append((nx,ny))
                
                elif visited[y][x][1] == 0 and visited[ny][nx][1] == 1 and visited[ny][nx][0] != 0 and g[ny][nx] == 0:# 벽 안뚫은 애가 벽뚫고 방문한 곳 만났을  때
                    visited[ny][nx][0] = visited[y][x][0] +1
                    visited[ny][nx][1] = visited[y][x][1]
                    queue.append((nx,ny))

                elif visited[y][x][1] == 1 and visited[ny][nx][1] == 1 and visited[y][x][0]+1 < visited[ny][nx][0] :#벽뚫은 애가 벽 뚫고 방문한 곳 만났는데 거리가 더 짧을 때
                    visited[ny][nx][0] = visited[y][x][0] +1
                    visited[ny][nx][1] = visited[y][x][1]
                    queue.append((nx,ny))         

                elif visited[ny][nx][0] == 0 and g[ny][nx] == 0:    #일반적인 진행.
                     visited[ny][nx][0] = visited[y][x][0] + 1
                     visited[ny][nx][1] = visited[y][x][1]
                     queue.append((nx,ny))

    if not queue : return -1  #목적지 도착 못했는데 갈 곳 없으면 -1 반환

print(sol(g,visited))