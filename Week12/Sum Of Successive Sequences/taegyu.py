def solution(sequence, k):
    answer = []
    s = 0
    start = len(sequence)-1
    
    for i in range(len(sequence)-1, -1, -1):
        s += sequence[i]

        if s > k:
            s -= sequence[start]
            start -= 1

        if s == k:
            answer.append([i, start, start-i])
            
    answer.sort(key=lambda x : (x[2], x[0]))
    return [answer[0][0], answer[0][1]]