import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())

pq = []
schedule = [0]*1001
for _ in range(n):
    d, w = map(int, input().split())
    heappush(pq, (-w, d))

for _ in range(n):
    w, d = map(abs, heappop(pq))
    while schedule[d] != 0 and d >= 0:
        d -= 1
    if d >= 0:
        schedule[d] = w

print(sum(schedule[1:]))