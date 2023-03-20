#처음 코드 -> 시간초과 뜸
def solution(X, Y):
    answer = ''
    a = sorted(str(X))
    b = sorted(str(Y))
    lst = []
    for i in a:
        if i in b:
            lst.append(int(i))
            del b[b.index(i)]
    lst.reverse()
    if len(lst) == 0:
        answer = "-1"
    #sum 쓰려면 int 형태 
    elif sum(lst) == 0:
        answer = "0"
    else:
        answer = ''.join(map(str,lst))
    #join 하려면 str형태
    return answer


#for문 9에서부터 시작해서 숫자 count해서 적은거 골라서 answer에 삽입하면 큰 숫자부터 앞에 주루룩
def solution(X, Y):
    answer = ''
    for i in range(9,-1,-1):
        answer = answer + min(X.count(str(i)), Y.count(str(i))) * str(i)
    if answer == '':
        return '-1'
    elif answer[0] == '0':
        return '0'
    return answer