# 1637
def solution(food):
    answer = ''
    for idx, val in enumerate(food):
        for i in range(val//2):
            answer+=str(idx)
    answer=answer + "0" + "".join(reversed(answer))

    return answer

def main():
    hi=[1,3,4,6]
    print(solution(hi))

if __name__=="__main__":
    main()