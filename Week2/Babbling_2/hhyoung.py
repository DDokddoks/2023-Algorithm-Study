# 1050
def solution(babbling):
    answer = 0
    spell = ["aya", "ye", "woo", "ma"]

    answer=len(babbling)
    for i in range(len(babbling)):
        for word in spell:
            babbling[i]=babbling[i].replace(word,'',1)
                
                
    print(babbling)
    answer-=len(babbling)  
    return answer

def main():
    print(solution(["aya", "yee", "u", "maa"]))


if __name__=="__main__":
    main()