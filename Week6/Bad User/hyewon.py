import re
from itertools import product

def solution(user_id, banned_id):
    banned_lst = [[] for _ in range(len(banned_id))]

    for idx, banned in enumerate(banned_id):
        tmp = banned.replace('*', '[a-z0-9]')
        pattern = re.compile(tmp + '$')
        for user in user_id:
            if pattern.match(user):
                banned_lst[idx].append(user)

    combs = list(product(*banned_lst))
    sets = []
    for comb in combs:
        if len(comb) == len(set(comb)):
            sets.append(tuple(sorted(comb)))
    return len(set(sets))
