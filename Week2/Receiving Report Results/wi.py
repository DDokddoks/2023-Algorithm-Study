def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reported = {id: 0 for id in id_list}
    report = [i.split() for i in set(report)]

    for i in report: reported[i[1]] += 1
    for i in report:
        if reported[i[1]] >= k: answer[id_list.index(i[0])] += 1

    return answer
