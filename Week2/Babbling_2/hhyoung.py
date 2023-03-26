# 1626
def solution(babbling):
    answer = 0
    spell = ["aya", "ye", "woo", "ma"]

    for idx,value in enumerate(babbling):
        if value in spell:
            if value==1:
                answer+=1
            elif value != babbling[idx-1]:
                answer+=1

    return answer