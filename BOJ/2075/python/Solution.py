import sys
import heapq

IN = sys.stdin.readline
N = int(input())
tile = list()

for _ in range(N):
    for i in list(map(int,IN().split())):
        heapq.heappush(tile, i)     #우선순위 큐로 push

        if len(tile)> N : heapq.heappop(tile)    #메모리 초과나서 배열 길이 5개로 유지. 배열길이 6일 때 제일 작은 수 pop

print(heapq.heappop(tile))