from collections import defaultdict


def solution(tickets):
    answer = []
    stack = ['ICN']
    routes = defaultdict(list)

    for ticket in tickets:
        src, dst = ticket[0], ticket[1]
        routes[src].append(dst)

    for src, values in routes.items():
        routes[src] = sorted(values, reverse=True)

    while stack:
        cur = stack[-1]
        if (cur not in routes) or (not routes[cur]):
            answer.append(stack.pop())
        else:
            stack.append(routes[cur].pop())

    return answer[::-1]
