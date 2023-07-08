def solution(elements):
    sums = set()
    for i in range(len(elements)):
        sequence = elements[i:] + elements[:i]
        for count in range(1, len(sequence) + 1):
            sums.add(sum(sequence[:count]))
    return len(list(sums))
