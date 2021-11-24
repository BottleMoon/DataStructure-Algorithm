N = int(input())    

def movie_title(i) :
    count = 0
    current = 666

    while (True):
        if str(current).find('666') != -1: 
            count+=1     #현재 숫자에  666이 포함되어있으면 count + 1

            if count == i or i == 0 : break

            if len(str(current))-str(current).find('666') == 3 :    # 666이 맨 오른쪽에 있을 때

                if len(str(current)) >= 4 and str(current)[-4] == '5' : #천의 자리 수가 5 일때.

                    if len(str(current)) >= 5 and str(current)[-5] =='6' : current += 333 #65666 이면 66000 으로 바로 만듬
                    else : current += 993     #만의 자리 수가 6이 아닐 경우 5666을  6660으로 바로 만듬

                else : current += 999 #천의 자리 수가 5가 아닐 때 바로 1000을 더함

        current += 1
    
    return current
    
print(movie_title(N))