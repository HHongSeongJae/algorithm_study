N = int(input())

numList = []

for _ in range(N):
    numList.append(list(map(int,input().split())))
    
for i in range(len(numList)):
    ranking = 1
    for j in range(len(numList)):
        if(numList[j][0]>numList[i][0]and numList[j][1]>numList[i][1]):
            ranking+=1
        print(ranking)

    



        
        
    