from collections import Counter
def solution(want, number, discount):
    answer = 0
    wants = Counter({want[i]:number[i] for i in range(len(want))})
    for i in range(len(discount) - 10 + 1):
        discounts = discount[i:i+10]
        counts = Counter(discounts)
        if not counts - wants:
            answer += 1
    return answer
