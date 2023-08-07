from itertools import product

def solution(n, info):
    answer = [-1]
    max_diff = 0
    info = info[::-1]

    for case in list(product([True, False], repeat=11)):
        total = sum([info[i]+1 for i in range(11) if case[i]])
        if total <= n:
            apeach = sum(i for i in range(11) if info[i] and not case[i])
            lion = sum(i for i in range(11) if case[i])
            diff = lion - apeach
            if max_diff < diff:
                max_diff = diff
                answer = [info[i]+1 if case[i] else 0 for i in range(11)]
                answer[0] += n-total

    return answer[::-1]