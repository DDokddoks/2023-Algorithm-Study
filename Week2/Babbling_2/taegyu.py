def check(s):
    possible = ["aya", "ye", "woo", "ma"]
    
    for each in possible:
        if each * 2 not in s:
            s = s.replace(each, ' ')
                
    return False if s.replace(' ', '') else True
        
def solution(babbling):
    answer = 0
    for s in babbling:
        if check(s): answer += 1
    return answer