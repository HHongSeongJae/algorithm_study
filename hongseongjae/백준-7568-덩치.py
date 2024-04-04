T = int(input())

member = []  # 사람에 대한 정보 저장
rank = []   # 등수 정보 저장

for i in range(T):
    x,y = map(int,input().split())
    member.append([x,y])

for i in range(T):
    count = 0
    for j in range(T):
        if (member[j][0] > member[i][0] ) and (member[j][1] > member[i][1]): 
            count += 1 #몸무게,키 나보다 큰사람 존재하는 인원 수 카운트
    rank.append(count + 1) #나의 등수는 +1 이 된다

print(*rank)