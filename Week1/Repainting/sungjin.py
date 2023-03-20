def solution(n, m, section):
    answer = 0
    num = 0
    for i in section:
        #num은 연속으로 덧칠할수 있는 범위
        if i > num:
            #i 가 num보다 크면 덧칠할 수 있는 범위 넘어갔으므로
            #answer 1 더하고 num(범위) 업데이트
            answer += 1
            num = i + m - 1
    return answer