# 1050
def solution(babbling):
    answer = 0
    spell = ["aya", "ye", "woo", "ma"]

    i=0
    while i<len(babbling):
        exWord=""
        j=0
        while j<len(spell): # spell의 각 원소의 길이만큼 babbling[]을 탐색후 삭제
            if babbling[i].find(spell[j], 0, len(spell[j])) != -1:
                if spell[j]==exWord:
                    break
                babbling[i]=babbling[i].replace(spell[j],"",1)
                exWord=spell[j]
                j=0 # 삭제 성공시 spell의 맨 첫번째 원소부터 다시 체크
            else:
                j+=1
        i+=1

    for word in babbling:
        if word=="":
            answer+=1
    print(babbling)
    return answer