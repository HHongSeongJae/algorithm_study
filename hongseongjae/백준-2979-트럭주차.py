a,b,c = map(int,input().split())

check = [0 for i in range(100)]  # 최대 입력이 100이기 때문에 100까지 리스트 초기화
check_maxnum = 0   # 입력된 값 중 가장 늦게 나가는 차량의 수를 찾는 변수

for i in range(3):
    enter, out = map(int, input().split())

    if check_maxnum < out: check_maxnum = out   # 가장 늦게 나가는 차량의 시간 확인

    for j in range(enter, out):   # 출차 시간을 확인하기 위한 check 리스트에 값 추가
        check[j] += 1
    
cost = 0
for idx, z in enumerate(check):
    if idx == check_maxnum:    # 가장 마지막으로 나가는 차량의 시간이 되면 반복문 탈출
        break

    #해당시간에 존재하는 차량 및 차량대수에 맞는 주차비 계산
    if z == 1:
        cost += a * z
    elif z == 2:
        cost += b * z
    else:
        cost += c * z

print(cost)