def all_zeros_bitwise(arr):
    return not any(arr)

def solution(want, number, discount):
    answer = 0
    count = {}

    for i, item in enumerate(want):
        count[item] = number[i]
    
    window = 0
    for i, item in enumerate(discount):
        window += 1
        if item in count:
            count[item] -= 1
        if window > 10 and discount[i-10] in count:
            count[discount[i-10]] += 1

        if all_zeros_bitwise(count.values()):
            answer += 1
    
    for i in range(len(discount)-10, len(discount)):
        if discount[i] in count:
            count[discount[i]] += 1
        if all_zeros_bitwise(count.values()):
            answer += 1

    return answer