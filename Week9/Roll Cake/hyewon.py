from collections import Counter
def solution(topping):
    answer = 0
    counter = Counter(topping)
    left_toppings = set()
    right = len(counter)
    for t in topping:
        counter[t] -= 1
        if counter[t] == 0:
            right -= 1
        left_toppings.add(t)

        if len(left_toppings) == right: answer += 1
    return answer
