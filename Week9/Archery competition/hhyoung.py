from itertools import combinations_with_replacement, permutations

def solution(n, info):
    answer = []
    for i in range(11): info[i] *= -1
    # arrowComb: 화살 수 조합
    for arrowComb in combinations_with_replacement([0,1,2,3,4,5,6,7,8,9,10], 11):
        if sum(arrowComb) == n:
            arrowComb = list(arrowComb)
            while 0 in arrowComb: arrowComb.remove(0)
            nInfo = info[:]
            # idxList: 화살이 꽂힌 점수의 조합
            for idxLst in permutations([0,1,2,3,4,5,6,7,8,9,10], len(arrowComb)):
                for i, v in enumerate(idxLst):
                    nInfo[v] += arrowComb[i]
                result = 0
                for i, v in enumerate(nInfo):
                    result += (10-i) * v
                if result > 0:
                    for i, v in enumerate(nInfo):
                        if v == -1: nInfo[i] = 0
                    answer.append(nInfo)
                nInfo = info[:]
    if not answer:
        return [-1]
    a = sorted(answer, reverse=True)
    return a[1]