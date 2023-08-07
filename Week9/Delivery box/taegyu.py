def solution(order):
    answer = 0
    
    idx = 0
    box_num = 1
    stk = []

    while box_num <= len(order):
        if order[idx] == box_num:
            answer += 1
            idx += 1
            box_num += 1
        elif stk and stk[-1] == order[idx]:
            stk.pop()
            answer += 1
            idx += 1
        else:
            stk.append(box_num)
            box_num += 1

    for num in stk[::-1]:
        if num == order[idx]:
            answer += 1
            idx += 1
        else:
            break

    return answer

print(solution([2, 1, 4, 3, 6, 5, 8, 7, 10, 9]))