from collections import deque

def solution(n, computers):
    answer = 0

    for i in range(n):
        computers[i][i] = 0

    visited = [False]*n
    for i in range(n):
        if not visited[i]:
            q = deque([i])
            while q:
                curr = q.popleft()
                for j in range(n):
                    if not visited[j] and computers[curr][j]:
                        visited[j] = True
                        q.append(j)
            answer += 1
            

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))