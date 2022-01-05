import sys
IN = sys.stdin.readline
sys.setrecursionlimit(10**6)

def changeToPostorder(arr):  
    root = arr[0]     #루트 노드
    point = len(arr)
    for i, v in enumerate(arr):
        if v > root:
            point = i;
            break;

    if point > 1:
        changeToPostorder(arr[1:point])   #루트 왼쪽
    if point != len(arr):
        changeToPostorder(arr[point:])    #루트 오른쪽
    print(root)   #프린트


arr = list()

while True:     #입력 받아옴
    try:
        arr.append(int(IN()))
    except:
        break

changeToPostorder(arr)