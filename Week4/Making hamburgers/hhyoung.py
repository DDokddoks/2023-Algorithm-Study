def solution(ingredient):
    answer = ham = 0
    ham_set = [1,2,3,1]
    list_ham = []
    
    for food in ingredient:
        list_ham.append(food)
        list_ham_len = len(list_ham)
        if list_ham_len >= 4:
            if ham_set == list_ham[list_ham_len-4:list_ham_len]:
                answer += 1
                for i in range(4):
                    list_ham.pop()

    return answer