import sys
IN = sys.stdin.readline
N = int(IN())

match = dict()

for _ in range(N):
    s = IN().strip()    #입력 받음

    for i in range(len(s)):     #알파벳마다 가중치 입력
        if s[i] not in match:
            match[s[i]] = 0
        match[s[i]]+=10**(len(s)-i-1)

# 가중치를 기준으로 정렬
val_list = list(match.values())
val_list.sort(reverse=True) 

sum = 0

#가중치 큰 알파벳부터 9, 8, 7 차례로 곱해서 sum에 합침
for i in range(len(val_list)):
    sum += val_list[i]*(9-i)

print(sum)