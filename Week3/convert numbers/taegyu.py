from collections import deque

def solution(x, y, n): 
    answer = -1
    q = deque([(x, 0)])
    dp = [0]*(y+1)
    
    while q:
        curr, cnt = q.popleft()
        if curr == y:
            answer = cnt
            break
        else:
            if curr+n <= y and not dp[curr+n]:
                dp[curr+n] = cnt+1
                q.append((curr+n, cnt+1))
            if curr*2 <= y and not dp[curr*2]:
                dp[curr*2] = cnt+1
                q.append((curr*2, cnt+1))
            if curr*3 <= y and not dp[curr*3]:
                dp[curr*3] = cnt+1
                q.append((curr*3, cnt+1))
        
    return answer