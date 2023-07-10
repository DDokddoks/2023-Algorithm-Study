from collections import defaultdict

def solution(k, tangerine):
    answer = 0
    types = defaultdict(int)
    for each in tangerine:
        types[each] += 1
    
    for count in sorted(list(types.values()), reverse=True):
        k -= count
        answer += 1
        if k <= 0: break
        
    return answer