def solution(X, Y):
    answer = ""
    partner = set(X) & set(Y)
    
    if not partner: return "-1"
    if len(partner) == 1 and '0' in partner: return "0"

    for i in sorted(partner, reverse=True):
        answer += str(i) * min(X.count(i), Y.count(i))
    return answer
