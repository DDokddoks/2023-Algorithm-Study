def solution(ingredient):
    answer, i = 0, 0
    
    while i <= (len(ingredient)-4):
        if [1, 2, 3, 1] == ingredient[i:i+4]:
            del ingredient[i:i+4]
            answer, i = answer + 1, i - 3
        i += 1
        
    return answer
