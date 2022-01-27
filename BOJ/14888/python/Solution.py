import sys
from collections import deque
IN = sys.stdin.readline;
N = int(IN())

num_list = list(map(int,IN().split()))
simbol = list(map(int,IN().split()))

max = None
min = None

#계산기
def calculator(stack) :
    result = num_list[0]
    for n in range(len(stack)):
        if stack[n] == 0:
            result += num_list[n+1]
        elif stack[n] == 1:
            result -= num_list[n+1]
        elif stack[n] == 2:
            result *= num_list[n+1]
        else :
            if result < 0 :
                result = -((-result) // num_list[n+1])
            else :
                result //= num_list[n+1]
    return result

#DFS 탐색
def dfs(stack =deque(), simbol = simbol):

    global max, min
    if len(stack) == N-1:
        result = calculator(stack)
        if max == None or max < result: max =result
        if min == None or min > result: min = result

    for i in range(4):
        if simbol[i] > 0 :
            stack_copy = stack.copy()
            simbol_copy = simbol.copy()
            stack_copy.append(i)
            simbol_copy[i] -= 1;
            dfs(stack_copy, simbol_copy)

dfs()
print(max)
print(min)