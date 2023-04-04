import heapq

def solution(n, k, enemy):    
    answer = 0
    sum = 0
    max_heap = []
    
    for i in enemy:
        heapq.heappush(max_heap, (-i, i))
        sum += i
        #sum이 n보다 크면 무적권 사용
        if sum > n:
            #sum이 큰데 무적권 없으면 끝
            if k == 0:
                break
            sum -= heapq.heappop(max_heap)[1]
            #무적권 쓰면 k -> --
            k -= 1
        answer += 1
    return answer