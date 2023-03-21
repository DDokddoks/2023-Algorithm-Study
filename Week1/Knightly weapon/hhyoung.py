def solution(number, limit, power):
    answer = 0

    for i in range(1,number+1):
        num=1
        for j in range(1,i//2+1):
            if i%j==0:
                num+=1
        if num>limit:
            answer+=power
        else :
            answer+=num            
        print(answer)

    return answer