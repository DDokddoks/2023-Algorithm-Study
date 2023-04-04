import heapq

def solution(n, k, enemy):
    skill = enemy[:k]
    heapq.heapify(skill)
    
    for i, e in enumerate(enemy[k:]):
        n -= heapq.heappushpop(skill, e)
        if n < 0: return i + k
    
    return len(enemy)