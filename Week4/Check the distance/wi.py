def is_valid(x, y):
    return x >= 0 and x < 5 and y >= 0 and y < 5


def check(place):
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for i, p in enumerate(place):
        for j, e in enumerate(p):
            if e == "P":
                if any([place[i+dx][j+dy] == 'P' for dx, dy in move if is_valid(i+dx, j+dy)]): 
                    return 0
            
            elif e == "O":
                if [place[i+dx][j+dy] == 'P' for dx, dy in move if is_valid(i+dx, j+dy)].count(True) > 1: 
                    return 0
    
    return 1


def solution(places):
    return [check(place) for place in places]
