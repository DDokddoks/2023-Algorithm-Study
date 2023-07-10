def solution(elements):
    sums = set(elements)
    extended = elements * 2
    
    for i in range(len(elements)):
        for j in range(2, len(elements)+1):
            sums.add(sum(extended[i:i+j]))
    
    return len(sums)