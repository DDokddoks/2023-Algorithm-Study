def getDivCount(n, limit, power):
    cnt = 0 
    for i in range(1, int(n**(1/2))+1):
        if i*i == n: cnt += 1
        elif n % i == 0: cnt += 2
        if cnt > limit: return power
    return cnt

def solution(number, limit, power):
    return sum(getDivCount(i, limit, power) for i in range(1, number+1))
