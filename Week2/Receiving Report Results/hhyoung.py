def solution(id_list, report, k):
    answer = []
    
    i_rep={id:[0] for id in id_list} # {이름:[(정지메일 받은 횟수)0, "본인이 신고한 사람들", ...]}
    me_rep={id:0 for id in id_list}  # {이름:0 (자신이 신고당한 횟수) }
    
    for str in report:
        id=str.split()
        if id[1] not in i_rep[id[0]]:
            i_rep[id[0]].append(id[1])
            me_rep[id[1]]+=1

    for id in id_list:
        if me_rep[id]>=k:
            for key,v in i_rep.items():
                if id in i_rep[key]:
                    i_rep[key][0]+=1

    for id in id_list:
        answer.append(i_rep[id][0])

    return answer