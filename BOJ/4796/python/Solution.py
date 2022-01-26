import sys
IN = sys.stdin.readline
case_list = list()
count = 0

while True:
    count += 1
    result = 0
    x = IN().strip()

    if x == '0 0 0': break  # 0 0 0이면 중지

    x = list(map(int,x.split()))
    
    result = x[2]//x[1]*x[0]

    if x[2]%x[1] < x[0] : result += x[2]%x[1]
    else : result += x[0]

    case_list.append('Case {0}: {1}'.format(count,result))

for s in case_list:
    print(s)