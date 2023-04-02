import heapq

def solution(n, k, enemy):
    l = len(enemy)
    if k >= l: return l

    skill = enemy[:k]
    heapq.heapify(skill)
    
    for i in range(k, l):
        n -= heapq.heappushpop(skill, enemy[i])
        if n < 0: return i
    
    return l
