#1305
def solution(today, terms, privacies):
    answer = []
    valid={i.split()[0]:int(i.split()[1]) for i in terms}
    
    TY,TM,TD=(int(x) for x in today.split('.'))
    for idx,i in enumerate(privacies):
        date, option=i.split()
        YY,MM,DD=(int(x) for x in date.split('.'))

        DD-=1
        if DD<1:
            if MM==1:
                YY-=1
                MM=12
            else:
                MM-=1
            DD=28

        MM+=valid[option]
        if MM>12:
            YY+=MM//12
            MM%=12

        if TY>YY: answer.append(idx+1)
        elif TY==YY and TM>MM: answer.append(idx+1)
        elif TY==YY and TM==MM and TD>DD: answer.append(idx+1)
    return answer

def test(today):
    y,m,d=today.split('.')
    print(y,m,d)


def main():
    solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])
    

if __name__=="__main__":
    main()