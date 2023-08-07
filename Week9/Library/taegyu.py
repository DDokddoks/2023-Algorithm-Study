import sys
input = sys.stdin.readline

answer = 0
n, m = map(int, input().split())
locations = sorted(list(map(int, input().split())))

plus = []
minus = locations
for i in range(n):
    if locations[i] > 0:
        plus = locations[i:]
        minus = locations[:i]
        break
minus = list(map(abs, minus[::-1]))

for i in range(len(plus)-1, -1, -m): answer += plus[i] * 2
for i in range(len(minus)-1, -1, -m): answer += minus[i] * 2

if not minus or (plus and plus[-1] > minus[-1]):
    answer -= plus[-1]
elif not plus or (minus and plus[-1] < minus[-1]):
    answer -= minus[-1]

print(answer)