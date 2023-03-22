def solution(id_list, report, k):
    #key: 신고당한 사람(문자열), value: 신고한 사람 배열
    rep_info = {}
    #key : 메시지 받을 사람(문자열) value: 받을 횟수(정수)
    msg = {}

    for i in id_list:
        rep_info[i] = []
        msg[i] = 0
    #이중for문 -> 시간초과 find,index -> 런타임에러 해결
    for i in report:
        a,b = i.split()
        #rep_info[b] 의 value에 a가 없으면 추가(중복되면 추가 안함)
        if a not in rep_info[b]:
            rep_info[b].append(a)

        #rep_info 확인해서 길이가 k 이상이면 정지
        #메시지 보내기 위해서 k이상이면 rep_info의 value 확인해서 신고한 사람들을
        #새로운 딕셔너리 msg[신고한 사람] = 메시지 받을 횟수 로 저장
    for i in id_list:
        if len(rep_info[i]) >= k:
            for j in rep_info[i]:
                msg[j] += 1
                
    return list(msg.values())