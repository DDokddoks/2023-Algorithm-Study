from heapq import heappush, heappop # maxheap 사용

def solution(n, k, enemy):
    answer = 0
    heap = []
    e_sum = 0
    for i in enemy:
        heappush(heap, i)
        e_sum += i
        if e_sum > n:
            if k == 0:
                break
            e_sum -= heappop(heap)
            k -= 1
        answer += 1
    return answer
