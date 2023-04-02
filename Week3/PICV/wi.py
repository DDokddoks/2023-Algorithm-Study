def to_day(date, vaild = 0):
    year, month, day = map(int, date.split("."))
    return year * 28 * 12 + (month + vaild) * 28 + day

def solution(today, terms, privacies):
    terms = {t[0]: int(t[2:]) for t in terms} 
    today = to_day(today)
    return [i+1 for i, p in enumerate(privacies) if today >= to_day(p[:10], terms[p[-1]])]
