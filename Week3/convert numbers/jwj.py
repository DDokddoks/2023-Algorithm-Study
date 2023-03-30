# 동적 계획법, 메모이제이션
def solution(x, y, n):
    answer = 0
    memo = [1000001 for _ in range(0, 1000001)]
    memo[x] = 0
    # x부터 y에 도달할 때 까지 dp로 최소 횟수 카운트 시작
    for num in range(x, y + 1):
        memo[num] = min(memo[num - n] + 1, memo[num])   # n을 더하는 연산
        if num % 2 == 0:    # 2를 곱하는 연산
            memo[num] = min(memo[num // 2] + 1, memo[num])
        if num % 3 == 0:    # 3을 곱하는 연산
            memo[num] = min(memo[num // 3] + 1, memo[num])

    if memo[y] == 1000001:    # y를 만들 수 없다면 -1 반환
        answer = -1
    else:
        answer = memo[y]
    return answer
