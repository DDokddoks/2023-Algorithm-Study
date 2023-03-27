from itertools import product

def solution(users, emoticons):
    pl = [[int(emoticons[i]*(100 - j*10)/100) for j in range(1, 5)] for i in range(len(emoticons))] #할인 연산횟수 줄이기
    seq = list(product(range(3, -1, -1), repeat=len(emoticons))) #이모티콘별 가능한 할인 중복순열
    value_list = [[0, 0, 0, 0] for i in range(len(seq))] #중복순열에 따른 할인비율별 총 이모티콘 가격
    for i in range(len(seq)):
        for j in range(len(emoticons)): value_list[i][seq[i][j]] += pl[j][seq[i][j]] #0:10%, 1:20%...에 해당하는 인덱스에 가격 덧셈
        for j in range(2, -1, -1): value_list[i][j] += value_list[i][j+1] #더 작은 할인에 더 높은 할인가격 덧셈
    
    result = [[0, 0] for i in range(len(seq))]
    for i in range(len(seq)):
        for j in users:
            if value_list[i][(j[0]-1)//10] >= j[1]: result[i][0]+=1 #희망가격보다 높으면 가입자수 덧셈
            else: result[i][1] += value_list[i][(j[0]-1)//10] #희망가격보다 낮으면 가격 덧셈
    return max(i for i in result) #배열 중 최대 반환