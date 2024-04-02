'''
나라 순위 규칙

금메달 수가 더 많은 나라 
금메달 수가 같으면, 은메달 수가 더 많은 나라
금, 은메달 수가 모두 같으면, 동메달 수가 더 많은 나라 


한 국가의 등수는 (자신보다 더 잘한 나라 수) + 1

1번 국가가 금메달 1개, 은메달 1개를 얻었고, 2번 국가와 3번 국가가 모두 은메달 1개를 얻었으며, 
4번 국가는 메달을 얻지 못하였다면, 1번 국가가 1등, 2번 국가와 3번 국가가 공동 2등, 
4번 국가가 4등이 된다. 
이 경우 3등은 없다

[총 국가수][알고싶은 국가의 등수]
[국가 나타내는 정수] [금][은][동]
'''

N , K = map(int, input().split()) # m : 찾는 국가 번호

prize = [0 for i in range(4)]

for i in range(N):
    prize[i] = list(map(int,input().split()))

# prize = [list(map(int,input().split())) for _ in range(N)]

# print(prize)

prize.sort(key = lambda x: (x[1], x[2] , x[3]) , reverse=True)  # 메달의 수만 보고 정렬

# 찾는 국가의 인덱스 => 순위
idx = 0
for j in range(N):
    if(prize[j][0] == K):
        idx = j

# 동점 확인
for z in range(N):
    if prize[idx][1:] == prize[z][1:]:
        print(z+1)
        break

