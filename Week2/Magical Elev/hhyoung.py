def extract(idx, num):
    return num[idx]

def solution(storey):
    answer = 0
    numLen=len(str(storey))

    for i in range(numLen):
        if extract(i, storey)>5:


    return answer

1290
10 -300 -1000
1434
-4 -30 -400 - 1000
1273
-3 30 -300 -1000
7 2 -3 -1 

1674
-4 30 -700 -1000 = 15
6 20 300 -2000 = 13

8674
-4 30 +300 

1952
-2 +50 -2000

315
-5 -10 - 300

545
-5 -40 -500
5 -50 -500

59395
5 -400 +1000 -60000 = 16
+5 600 -6000 =17
0 4 -2 4 0

59495
5 -500 1000 -60000 =17
5 500 -60000 =16
# 1의 자리 수 부터 위로 쭉 조정해가는데 변동사항이 적용되어야함
1945 
# 예외. 큰 자리수부터 확인해야하나..? 5면 일단 넘어가 아 굳이 큰자리붵 

굳이 큰 자릿수부터 지울 생각 안해도될듯?
걍 단순히 그 자리에서 0에 가까운거로 맞추는게 낫네. 근데 5면 문제

각 자리수에 5와 차이를 기록하여 결정하면 될듯?