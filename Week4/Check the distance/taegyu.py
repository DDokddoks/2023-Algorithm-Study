from collections import deque

def bfs(room, p_pos):
    diff = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 위에서부터 시계 방향으로 확인
    
    for x, y in p_pos:
        q = deque([(x, y)])
        temp = deque()
        distance = 0
        visited = [[False]*5 for _ in range(5)]
        
        while q:
            distance += 1
            if distance > 2: break
            temp = q.copy()
            q.clear()
            
            while temp:
                cx, cy = temp.popleft()           
                visited[cx][cy] = True
                
                for dx, dy in diff:
                    nx, ny = cx+dx, cy+dy
                    if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                        if room[nx][ny] == 'P': return False 
                        if room[nx][ny] == 'O': q.append((nx, ny))
    return True

def solution(places):
    answer = []
    for room in places:     
        p_pos = [(x, y) for x in range(5) for y in range(5) if room[x][y] == 'P']
        answer.append(1 if bfs(room, p_pos) else 0)
        
    return answer