import sys
IN = sys.stdin.readline

N, M = map(int,IN().split())
g = [0 for _ in range(N)]

dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]

for i in range(N):
    g[i] = [int(i) for i in list(IN())[:M]]
 
visited = [[0] * M for _ in range(N)]


def sol(g, visited):
    queue = [(0,0)]
    while(queue):
        x, y = queue.pop(0)
        
        if x == N-1 and y == M-1:
            return (visited[x][y]) +1
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0 and g[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))

print(sol(g,visited))