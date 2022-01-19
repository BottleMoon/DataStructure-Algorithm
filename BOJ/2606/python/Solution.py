import sys
IN = sys.stdin.readline

com_no = int(IN()) #컴퓨터 개수
line_no = int(IN()) #간선 개수
check = dict() 
web = dict()

for i in range(1,com_no+1):
    web[i] = set()
    check[i] = [0,0]    #[visited, isInfected]

for _ in range(line_no):
    x, y = map(int,IN().split())
    web[x].add(y)
    web[y].add(x)

#dfs
def sol(com) :
    check[com][0] = 1
    for i in web[com]:
        if check[i][0] == 0:
            check[i][1] = 1
            sol(i)

sol(1)
count = 0
for i in check:
    if check[i][1] == 1:
        count+=1
print(count)