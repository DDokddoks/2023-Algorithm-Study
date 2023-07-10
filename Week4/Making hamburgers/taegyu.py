def solution(ingredient):
    answer = 0
    std = [1, 2, 3, 1]
    stk = ingredient[:4]
    
    for each in ingredient[4:]+[0]:
        if stk[-4:] == std:
            answer += 1
            # del stk[-4:]
            for i in range(4): stk.pop()    # pop이 조금 더 빠름
        stk.append(each)
    return answer