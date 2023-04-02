def solution(today, terms, privacies):
    answer = []
    di = {}
    ty, tm, td = map(int, today.split('.'))
    
    for info in terms:
        term, period = info.split(" ")
        di[term] = int(period)
        
    for i, p in enumerate(privacies):
        date, term = p.split(" ")
        period = di[term]
        y, m, d = map(int, date.split('.'))
        
        m += period
        while m > 12:
            y += 1
            m -= 12
        
        if y > ty: continue
        elif y < ty: answer.append(i+1)
        else:
            if m > tm: continue
            elif m < tm: answer.append(i+1) 
            else:
                if d > td: continue
                else: answer.append(i+1)
        
    return answer