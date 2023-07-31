import sys
input = sys.stdin.readline

# Python3는 시간초과, PyPy3는 통과
def solution():
    r, c, t = map(int, input().split())
    room = [list(map(int, input().split())) for _ in range(r)]

    cleaner = []
    for i in range(r):
        if room[i][0] == -1:
            cleaner.append(i)

    def dust_diffusion():
        # 미세먼지 확산
        dust = [[0] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if room[i][j] >= 5:
                    spread = room[i][j] // 5
                    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        nx, ny = i+dx, j+dy
                        if 0 <= nx < r and 0 <= ny < c and room[nx][ny] != -1:
                            dust[nx][ny] += spread
                            room[i][j] -= spread
        
        for i in range(r):
            for j in range(c):
                room[i][j] += dust[i][j]

    def cleaner_upper():
        # 공기청정기 작동
        # 위쪽
        for i in range(cleaner[0]-1, 0, -1):
            room[i][0] = room[i-1][0]
        for i in range(c-1):
            room[0][i] = room[0][i+1]
        for i in range(cleaner[0]):
            room[i][c-1] = room[i+1][c-1]
        for i in range(c-1, 1, -1):
            room[cleaner[0]][i] = room[cleaner[0]][i-1]
        room[cleaner[0]][1] = 0

    def cleaner_bottom():
        # 아래쪽
        for i in range(cleaner[1]+1, r-1):
            room[i][0] = room[i+1][0]
        for i in range(c-1):
            room[r-1][i] = room[r-1][i+1]
        for i in range(r-1, cleaner[1], -1):
            room[i][c-1] = room[i-1][c-1]
        for i in range(c-1, 1, -1):
            room[cleaner[1]][i] = room[cleaner[1]][i-1]
        room[cleaner[1]][1] = 0

    
    for _ in range(t):
        dust_diffusion()
        cleaner_upper()
        cleaner_bottom()

    # 2로 초기화하여 공기청정기에 해당하는 -2 상쇄
    answer = 2
    for line in room:
        answer += sum(line)

    print(answer)

solution()