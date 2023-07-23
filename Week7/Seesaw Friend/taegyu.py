from collections import Counter

def solution(weights):
    possible = [2/3, 2/4, 3/4]
    counts = Counter(weights)
    answer = 0
    
    for w in set(weights):
        for p in possible:
            if w*p in weights:
                answer += counts[w] * counts[w*p]
    
    for value in counts.values():
        if value > 1:
            answer += value*(value-1)//2

    return answer

print(solution([100,180,360,100,270]))