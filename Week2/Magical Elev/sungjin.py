def solution(storey):
    answer = 0

    while storey != 0:
        print(storey)
        div = storey % 10
        #5보다 크면 위로
        if div > 5:
            answer += 10 - div
            storey += 10 - div
        #5면 뒷 자리 확인후 위나 아래
        elif div == 5:
            if (storey // 10) % 10 >= 5:
                storey += 10 - div
            else:
                storey -= div
            answer += div
        #5보다 작으면 아래로
        else:
            answer += div
            storey -= div
        print(storey)
        storey //= 10
        
    return answer

#storey +- 처리 안하고 10으로 나누기만 해서 틀림 -> 나눴을 때 0이 되야 종료되므로