def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reported = {id: 0 for id in id_list}
    report = [r.split() for r in set(report)]
    
    for u, r in report: reported[r] += 1
    for u, r in report: 
        if reported[r] >= k: answer[id_list.index(u)] += 1

    return answer
