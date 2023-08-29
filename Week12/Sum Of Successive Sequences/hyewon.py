def solution(sequence, k):
    answer = []
    s, e = 0, 0
    total = sum(sequence[s:e+1])
    while s <= e < len(sequence):
        if total == k:
            answer.append((s, e))
            total -= sequence[s]
            s += 1
        elif total < k:
            if e + 1 == len(sequence): break
            e += 1
            total += sequence[e]
        else:
            total -= sequence[s]
            s += 1

    answer.sort(key=lambda x:(x[1] - x[0], x[0]))
    return answer[0]
