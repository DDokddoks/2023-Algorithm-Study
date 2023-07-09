from collections import Counter


def solution(k, tangerine):
    counts = 0
    answer = 0
    for t in Counter(tangerine).most_common():
        answer += 1
        counts += t[1]
        if counts >= k: break
    return answer
