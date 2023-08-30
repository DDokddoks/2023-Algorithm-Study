from collections import deque

def solution(board):
    answer = 0
    rows = len(board)
    cols = len(board[0])

    visited = [[False]*cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 'R':
                q = deque([(i, j)])

    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    while q:
        answer += 1
        temp = []
        for r, c in q:
            if board[r][c] == 'G':
                return answer-1

            visited[r][c] = True
            for d in directions:
                nr, nc = r, c
                while 0 <= nr+d[0] < rows and 0 <= nc+d[1] < cols and board[nr+d[0]][nc+d[1]] != 'D':
                    nr += d[0]
                    nc += d[1]
                
                if not visited[nr][nc]:
                    temp.append((nr, nc))

        q = deque(temp)

    return -1

print(solution([".D.R", "....", ".G..", "...D"]))