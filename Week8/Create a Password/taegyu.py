import sys
input = sys.stdin.readline

def solution():
    l, c = map(int, input().split())
    chars = sorted(input().split())
    vowels = ['a', 'e', 'i', 'o', 'u']

    def dfs(idx, password):
        if len(password) == l:
            if len(set(password) & set(vowels)) >= 1 and len(set(password) & (set(chars)-set(vowels))) >= 2:
                print(password)
            return
        
        for i in range(idx, c):
            dfs(i+1, password+chars[i])

    dfs(0, "")

solution()