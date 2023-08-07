from collections import Counter

def solution(topping):
    answer = 0

    first = dict()
    second = Counter(topping)

    first_len = 0
    second_len = len(second)

    for t in topping:
        second[t] -= 1
        if second[t] == 0: 
            second_len -= 1
        
        if t not in first:
            first[t] = 1
            first_len += 1

        if first_len == second_len:
            answer += 1
        
    return answer
        
