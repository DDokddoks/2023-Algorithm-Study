from collections import deque

def solution(maps):
    answer = 0

    q = deque([(0, 0)])

    while q:
        answer += 1
        for _ in range(len(q)):
            x, y = q.popleft()
            if x == len(maps[0])-1 and y == len(maps)-1:
                return answer
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < len(maps[0]) and 0 <= ny < len(maps) and maps[ny][nx] == 1:
                    maps[ny][nx] = 0
                    q.append((nx, ny))
    
    return maps[-1][-1] if maps[-1][-1] == 0 else -1