# 1050
def solution(babbling):
    answer = 0
    spell = ["aya", "ye", "woo", "ma"]

    exWord=""
    for i in range(len(babbling)):
        for word in spell:
            if babbling[i].find(word, 0, len(word)):
                if word==exWord:
                    break
                babbling[i]=babbling[i].replace(word,"",1)
                exWord=word
    if word in babbling:
        if word=="":
            answer+=1
    return answer

def main():
    print(solution(["aya", "yee", "u", "maa"]))


if __name__=="__main__":
    main()