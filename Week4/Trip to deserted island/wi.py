from collections import deque


def solution(maps):
    answer = []
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]

    def bfs(x, y):
        visited[x][y] = True
        q = deque([(x, y)])
        area = int(maps[x][y])

        while q:
            qx, qy = q.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = qx + dx, qy + dy
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and visited[nx][ny] == False and maps[nx][ny] != 'X':
                    visited[nx][ny] = True
                    area += int(maps[nx][ny])
                    q.append((nx, ny))

        return area

    for i, map in enumerate(maps):
        for j, m in enumerate(map):
            if m != 'X' and visited[i][j] == False:
                answer.append(bfs(i, j))

    return [-1] if len(answer) == 0  else sorted(answer)
