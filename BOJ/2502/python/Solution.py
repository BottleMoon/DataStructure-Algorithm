import sys
sys.setrecursionlimit(10**6)
IN = sys.stdin.readline

day, N = map(int,IN().split())

def sol(pre,now=N, day = day):
    if pre < 0 or now < 0:  #2일이 되기 전까지 음수가 나오면 탈락
        return

    if day == 2:
        print(pre)
        print(now)
        exit() #하나라도 찾으면 종료

    if now > pre*2 : return  # 2일이 되기 전까지 pre가 now/2 보다 작으면 탈락

    temp = now
    now = pre
    pre = temp - pre

    sol(pre, now, day-1)

for i in range(1,N//2+1):
    sol(N-i)