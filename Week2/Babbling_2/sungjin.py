def solution(babbling):
    answer = 0
    word = ["aya", "ye", "woo", "ma"]
    flag = 0
    #문자열을 각각 대응하는 숫자로 replace
    for i in range(4):
        for j in range(len(babbling)):
            babbling[j] = babbling[j].replace(word[i], str(i))
    
    #정수인지 확인 후 연속한다면 flag = 1, for문 돌려서 flag = 0이면 answer++
    for i in range(len(babbling)):
        flag = 0
        if babbling[i].isdigit():
            for j in range(len(babbling[i])-1):
                if babbling[i][j] == babbling[i][j+1]:
                    flag = 1
            if flag == 0:
                answer += 1
    return answer