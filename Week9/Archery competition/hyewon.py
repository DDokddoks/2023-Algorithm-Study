from itertools import combinations_with_replacement

def calc_score(a, b): # Apeach, Lion
    a_score, b_score = 0, 0
    for i in range(10):
        if a[i] == b[i] == 0: continue
        if a[i] >= b[i]:
            a_score += 10 - i
        else:
            b_score += 10 - i
    return a_score, b_score

def get_larger_list(a, b):
    for num1, num2 in zip(reversed(a), reversed(b)):
        if num1 > num2:
            return a
        elif num2 > num1:
            return b
    return b

def solution(n, info):
    answer = []
    max_diff = 0
    scores = [10 - i for i in range(0, 11)]
    for combs in combinations_with_replacement(scores, n):
        ryan = [0] * 11
        for c in combs:
            ryan[c] += 1
        apeach_score, ryan_score = calc_score(info, ryan)
        if apeach_score < ryan_score:
            diff = ryan_score - apeach_score
            if diff > max_diff:
                max_diff = diff
                answer = ryan
            elif diff == max_diff:
                answer = get_larger_list(answer, ryan)
    return answer if answer else [-1]
