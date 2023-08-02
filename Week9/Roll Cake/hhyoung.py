from collections import Counter, defaultdict
def solution(topping):
    answer = 0
    sis = defaultdict(int)
    sis[topping[0]]
    bro = Counter(topping[1:len(topping)])
    broLen = len(bro)
    if len(sis) == broLen: answer += 1

    for i in range(1, len(topping)-1):
        sis[topping[i]] += 1
        bro[topping[i]] -= 1
        if bro[topping[i]] == 0:
            bro.pop(topping[i])
            broLen -= 1
        if len(sis) == broLen: answer += 1

    return answer

# sis(동생)은 defaultdict bro(형)은 Counter
# 동생쪽 케익크기를 늘려가면서 체크하는거니까
# sis[topping[i]] += 1
# 형쪽은 bro[topping[i]] -= 1 한 후 해당 value값이 0이면 key 삭제
# 이후 sis와 bro의 케익 종류수 같으면 답 + 1