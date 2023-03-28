def solution(babbling):
    pattern = {"ayaaya": "#", "yeye": "#", "woowoo": "#", "mama": "#", 
               "aya": " ", "ye": " ", "woo": " ", "ma": " ", " ": ""}
    
    for k, v in pattern.items():
        babbling = list(map(lambda x: x.replace(k, v), babbling))
        
    return babbling.count("")
