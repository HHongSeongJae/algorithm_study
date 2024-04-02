P = int(input())

resultList=[]

for i in range(P):
    student = list(map(int,input().split()))
    count = 0
    for j in range(1, len(student)-1):
        for z in range(j+1, len(student)):
            if(student[z] < student[j]): 
                count+=1
            else:
                continue
    resultList.append([student[0], count])

for i in resultList:
    print(i[0],i[1])
    