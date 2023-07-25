def is_valid(rotated):
    stk = []
    
    for p in rotated:
        stk.append(p)
        if (len(stk) > 1 and 
            ((stk[-2] == '(' and stk[-1] == ')') or
             (stk[-2] == '{' and stk[-1] == '}') or
             (stk[-2] == '[' and stk[-1] == ']'))):
            stk.pop()
            stk.pop()
             
    return not stk

def solution(s):
    answer = 0
    
    for i in range(len(s)):
        if is_valid(s[i:]+s[:i]):
            answer += 1
        
    return answer