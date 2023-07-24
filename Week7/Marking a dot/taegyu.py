import math

def solution(k, d):
    answer = d // k * 2 + 1

    for x in range(k, d+1, k):
        max_y = int(math.sqrt(d**2 - x**2))
        answer += max_y // k

    return answer

print(solution(1, 5))