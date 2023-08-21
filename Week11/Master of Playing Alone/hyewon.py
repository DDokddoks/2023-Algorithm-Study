def solution(cards):
    answer = set()
    length = len(cards)
    cards = [0] + cards

    for idx in range(1, length + 1):
        opened = []
        while True:
            next_idx = cards[idx]
            opened.append(cards[idx])
            if cards[next_idx] in opened: break
            idx = next_idx
        answer.add(tuple(sorted(opened)))
    answer = sorted(list(answer), key=len)
    if len(answer) < 2: return 0
    return len(answer[-1]) * len(answer[-2])
