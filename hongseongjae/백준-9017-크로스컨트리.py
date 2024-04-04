## 첫번째 풀이 -> 동점인 경우를 고려하지 않았다.
T = int(input())

for i in range(T):
    N = int(input())
    rank = list(map(int,input().split()))

    team = max(rank) # 팀 수 확인
    result = [0 for i in range(team)]

    minus = 0

    for i in range(N): # i가 인덱스가 된다.
        # print(rank[i])
        if (rank.count(rank[i]) == 6):
            result[rank[i]-1] += i
            result[rank[i]-1] += minus
            minus = 0
        else:
            minus -= 1

    print(result.index(min(result)) + 1) # 동점자 처리 x  


## 풀이 참조코드
T = int(input())

for i in range(T):
    N = int(input())
    rank = list(map(int,input().split()))

    result = {}
    for i in range(N):
        if rank[i] in result: #이미 넣은 값
            result[rank[i]] += 1
        else: # 처음 등장한 팀
            result[rank[i]] = 1

    minus = {} #자격 미달 팀
    for a,b in result.items():
        if b < 6:
            minus[a] = 1


    score = {}  # [주자수, 점수합, 5번째 점수]
    idx = 1
    for i in range(N):
        if rank[i] not in minus: # 불합격 팀에 속하지 x
            if rank[i] in score:  # score에 기록된적이있음
                if score[rank[i]][0] < 4: # 4명 미만주자면
                    score[rank[i]][0] += 1
                    score[rank[i]][1] += idx #점수
                elif score[rank[i]][0] == 4:  
                    score[rank[i]][0] += 1
                    score[rank[i]][2] += idx # 5번째 사람의 점수
            else: # score에 첫 기록
                score[rank[i]] = [1, idx, 0]  # 최종적으로 값 입력
                
            idx += 1

    score = sorted(score.items(), key=lambda x:(x[1][1] , x[1][2]))

    print(score[0][0])

