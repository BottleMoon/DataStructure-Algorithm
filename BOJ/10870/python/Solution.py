N = int(input())    

def fib(i) :  
    if i <= 1:      #i가 0이면 0, 1이면 1 반환
        return i
    else:           #i가 2이상일 떄 i-1, i-2 재귀함수 호출해서 더함
        return fib(i-1) + fib(i-2)

print(fib(N))