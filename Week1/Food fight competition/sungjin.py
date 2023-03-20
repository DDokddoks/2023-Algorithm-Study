def solution(food):
    answer = '0'
    #처음에 food.index로 했다가 중복요소 인덱스 못찾아서 enumerate로 인덱스, 값 같이 사용
    for i,cnt in enumerate(food[:0:-1]):
        tmp = len(food) - i - 1
        answer = cnt//2 * str(tmp) + answer + cnt//2 * str(tmp)
    return answer