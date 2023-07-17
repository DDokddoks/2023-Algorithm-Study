def solution(plans):
    answer = []
    time_dict = {}

    for p in plans:
        time = list(map(int, p[1].split(':')))
        start_time = time[0] * 60 + time[1]
        time_dict[start_time] = [p[0], start_time, int(p[2])]

    stack = []
    for time in range(1440):
        if stack:
            stack[-1][2] -= 1
            if stack[-1][2] == 0:
                answer.append(stack.pop()[0])
        cur_study = time_dict.get(time)
        if cur_study:
            stack.append(cur_study)

    while stack:
        answer.append(stack.pop()[0])
    return answer
