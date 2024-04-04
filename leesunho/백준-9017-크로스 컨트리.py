T = int(input())

for _ in range(T):
    N = int(input())
    teamMember = list(map(int, input().split()))

    # 팀 별로 주자 수 세기
    teamItem = {}
    for member in teamMember:
        if member in teamItem:
            teamItem[member] += 1
        else:
            teamItem[member] = 1

    # 제외되는 팀 구하기
    for k, v in teamItem.items():
        if v < 6:
            teamMember = [x if x != k else 'n/a' for x in teamMember]

    # 점수 계산
    score = {}
    idx = 1  # 주자의 위치
    for member in teamMember:
        if member != 'n/a':
            if member in score:
                if score[member][0] < 4:
                    score[member][0] += 1
                    score[member][1] += idx
                elif score[member][0] == 4:
                    score[member][0] += 1
                    score[member][2] = idx
            else:
                score[member] = [1, idx, 0]  # [팀당 주자 수, 상위 4명 점수 합, 5번째 주자의 점수]

            idx += 1

    # 순위 정렬
    result = sorted(score.items(), key=lambda x: (x[1][1], x[1][2]))

    # 결과 출력
    print(result[0][0])
