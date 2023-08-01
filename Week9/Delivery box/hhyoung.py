from collections import deque
def solution(order):
    idx = 0
    # 주 컨테이너 벨트 ( 큐 )
    mainBelt = deque([i for i in range(1, len(order)+1)])
    # 보조 컨테이너 벨트 ( 스택 )
    sideBelt = deque()

    while idx < len(order):
        # 보조 벨트의 마지막이 쌓아야하는 짐일때
        if sideBelt and sideBelt[-1] == order[idx]:
            sideBelt.pop()
            idx += 1
        # 보조 벨트가 비었거나 쌓아야하는 짐이 아니고, 주 컨테이너 벨트도 비어있을때
        elif not mainBelt:
            break

        if mainBelt:
            # 컨테이너 벨트의 시작 부분이 쌓아야할 짐일때
            if mainBelt[0] == order[idx]:
                mainBelt.popleft()
                idx += 1
            # 보조 벨트도 컨테이너 벨트도 쌓아야할 짐이 아니라면 일단 보조벨트에 적재
            else:
                sideBelt.append(mainBelt.popleft())

    return idx