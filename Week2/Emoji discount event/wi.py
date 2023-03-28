from itertools import product


def calculate(users, emoticons, discount):
    cnt_user, sale_price = 0, 0
    
    for percent, price in users:
            cost = 0
            for i, emoticon in enumerate(emoticons):
                if (discount[i] >= percent):
                    cost += (emoticon * (100-discount[i])) // 100
                    
            if cost >= price: cnt_user += 1 
            else: sale_price += cost
            
    return cnt_user, sale_price


def solution(users, emoticons):
    reg_user, max_price  = 0, 0
    discounts = product([10, 20, 30, 40], repeat = len(emoticons))
    
    for discount in discounts:
        cnt_user, sale_price = calculate(users, emoticons, discount)
        
        if reg_user < cnt_user:
            reg_user, max_price = cnt_user, sale_price
        elif reg_user == cnt_user:
            max_price = max(max_price, sale_price)

    return [reg_user, max_price]
