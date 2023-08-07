import sys
input = sys.stdin.readline

# python3 시간초과, pypy3 통과
def check(x, y, num):
    for i in range(9):
        if sudoku[x][i] == num: return False
        if sudoku[i][y] == num: return False

    x = x // 3 * 3
    y = y // 3 * 3
    for i in range(x, x+3):
        for j in range(y, y+3):
            if sudoku[i][j] == num: return False

    return True

def dfs(idx):
    if idx == len(zeros):
        for row in sudoku:
            print(row)
        exit()

    x, y = zeros[idx]
    for i in range(1, 10):
        if check(x, y, str(i)):
            sudoku[x] = sudoku[x][:y] + str(i) + sudoku[x][y+1:]
            dfs(idx+1)
            sudoku[x] = sudoku[x][:y] + '0' + sudoku[x][y+1:]

sudoku = []
for _ in range(9):
    sudoku.append(input().strip())

zeros = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == '0':
            zeros.append((i, j))

dfs(0)