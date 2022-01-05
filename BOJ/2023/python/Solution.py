N = int(input())

# 계속 시간초과나서 구글링했더니 소수 판별을 잘못했었음
# 무식하게 2에서 n까지 다 나눠서 소수 확인 할 필요 없고 2에서 n의 제곱근까지만 나누면 소수 판별 된다고 함.

def is_prime(n) :       ## 소수인지 판별하는 함수
    if n == 1 : False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0 :
            return False
    return True

def print_special_prime(corrent, n):        ##dfs방식으로 print
    if not corrent < 10**N : return

    temp = int(corrent/10**n)
    max = (int(temp/10)+1)*10

    while temp < max:
        corrent = temp*10**n
        if is_prime(temp) :                     #10의 n승 까지의 숫자가 소수일 때
            if n == 0 : print(corrent)          #n이 0이면 출력
            else :print_special_prime(corrent, n-1)#0이 아니면 n-1해서 재귀
        temp += 1
 
start = 2 * 10 **(N-1)
print_special_prime(start,N-1)
