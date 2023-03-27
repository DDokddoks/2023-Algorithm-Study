def resursion(num):
    if num > 0:
        length = 10**(len(str(num))-1)
        opposite = abs(num-length*10)
        return min(resursion(num%length) + num//length, resursion(opposite%length) + opposite//length+1)
    else:
        return 0

def solution(storey):       
    return resursion(storey)