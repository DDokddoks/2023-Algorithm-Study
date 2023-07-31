def solution(fees, records):
    answer = []
    history = {}

    for record in records:
        time, car_num, state = record.split()
        if car_num not in history:
            history[car_num] = []
        history[car_num].append((time, state))

    for car_num in sorted(history.keys()):
        if len(history[car_num]) % 2 == 1:
            history[car_num].append(("23:59", "OUT"))
        
        total_time = 0
        for i in range(0, len(history[car_num]), 2):
            in_time = history[car_num][i][0].split(":")
            out_time = history[car_num][i+1][0].split(":")
            total_time += (int(out_time[0]) - int(in_time[0])) * 60 + (int(out_time[1]) - int(in_time[1]))

        if total_time <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + (total_time - fees[0]) // fees[2] * fees[3] + (1 if (total_time - fees[0]) % fees[2] != 0 else 0) * fees[3])

    return answer