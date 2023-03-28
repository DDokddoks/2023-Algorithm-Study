def getEdge(table):    
    start, end = 0, 0
    for i, line in enumerate(table):
        if '#' in line: 
            start = i
            break
            
    for i, line in enumerate(reversed(table)):
        if '#' in line: 
            end = len(table)-i
            break
            
    return start, end

def solution(wallpaper):
    lux, rdx = getEdge(wallpaper)
    luy, rdy = getEdge(list(zip(*wallpaper)))
        
    return [lux, luy, rdx, rdy]