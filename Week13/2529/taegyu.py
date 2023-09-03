import sys
input = sys.stdin.readline

def dfs(current, idx, iter):
    global answer, flag

    if idx == n+1: 
        answer = current
        flag = True

    if flag: return

    start, end, jump = iter
    for i in range(start, end, jump):
        if not flag and i not in current:
            if ((idx == 0) or
                (signs[idx-1] == '<' and current[idx-1] < i) or 
                (signs[idx-1] == '>' and current[idx-1] > i)):
                current[idx] = i
                dfs(current, idx+1, iter)

n = int(input())
signs = list(input().strip().split())
answer = None
flag = False

dfs([-1]*(n+1), 0, (9, -1, -1))
print(*answer, sep='')
flag = False
dfs([-1]*(n+1), 0, (0, 10, 1))
print(*answer, sep='')