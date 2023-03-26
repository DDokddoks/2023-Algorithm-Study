def solution(storey):
    answer = 0
    while storey != 0:
        mod, storey = storey % 10, round(storey/10)
        answer += mod if mod < 5 else 10 - mod
    return answer
