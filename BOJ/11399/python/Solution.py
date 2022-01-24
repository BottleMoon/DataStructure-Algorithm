import sys

IN = sys.stdin.readline
N = int(IN())
line = list(map(int,IN().split()))

line.sort()

result = 0 #기다린 시간 전체 합
sum = 0 #개인이 기다릴 시간

for i in line:
    sum += i
    result += sum

print(result)