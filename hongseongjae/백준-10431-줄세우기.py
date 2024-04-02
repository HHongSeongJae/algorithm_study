'''
항상 20명
키작은순 -> 큰순   같은키 x


자기 앞에 자기보다 키가 큰 학생이 없다면 그냥 그 자리에 서고 차례가 끝난다.
자기 앞에 자기보다 키가 큰 학생이 한 명 이상 있다면 그중 가장 앞에 있는 학생(A)의 바로 앞에 선다.
 이때, A부터 그 뒤의 모든 학생들은 공간을 만들기 위해 한 발씩 뒤로 물러서게 된다.

 줄서기 완료시 총 몇번 뒤로 물러섬?

'''

P = int(input())

for i in range(P):
    student = list(map(int,input().split()))
    count = 0

    for j in range(1, len(student)): # 1개 길게 나옴
        #구현
        ## 자기보다 앞에 확인
        for z in range(1, j):
            if(student[z] > student[j]): #앞에 큰 사람 존재
                temp = student[j]
                student.remove(student[j])
                student.insert(z, temp)
                
                count += abs(z-j)
            else:
                continue
    print(student[0], count)