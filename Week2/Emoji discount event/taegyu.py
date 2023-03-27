from itertools import product

def solution(users, emoticons):
    results = []
    discount = [10, 20, 30, 40]
    all_cases = product(discount, repeat=len(emoticons))
    
    for case in all_cases:
        plus, purchase = 0, 0
        for user in users:
            temp = 0
            for i in range(len(emoticons)):
                if user[0] <= case[i]: 
                    temp += int(emoticons[i]*(100-case[i])/100)
            
            if temp >= user[1]: 
                plus += 1
            else: 
                purchase += temp
        
        results.append((plus, purchase))
    
    return sorted(results)[-1]