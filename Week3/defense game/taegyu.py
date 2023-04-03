import heapq

def solution(n, k, enemy):
    answer = k
    min_heap = enemy[:k]
    heapq.heapify(min_heap)
    
    for e in enemy[k:]:
        heapq.heappush(min_heap, e)
        n -= heapq.heappop(min_heap)
        if n >= 0:
            answer += 1
        else:
            return answer
        
    return len(enemy)