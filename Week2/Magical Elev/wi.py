def solution(storey):
    answer = 0
    while storey != 0:
        div, mod = divmod(storey, 10) 
        storey = div + 1 if mod > 5 or (mod == 5 and div % 10 >= 5) else div  
        answer += mod if mod < 5 else 10 - mod
    return answer