N = int(input())
from collections import deque
cards = deque()
for i in range(N):
    cards.append(i+1)

while len(cards) >1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards.pop())