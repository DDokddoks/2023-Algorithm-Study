def solution(n):
    answer = 1
    while n != 1:
        if n % 2 == 0: # 순간이동
            n //= 2
        else: # 점프
            n -= 1
            answer += 1
    return answer