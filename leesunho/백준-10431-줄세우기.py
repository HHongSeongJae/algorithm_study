P = int(input())

resultList  = []


for p in range(P):
    result = 0
    a = list(map(int,input().split()))
    for i in range(1, len(a)-1):
        for j in range(i+1, len(a)):
            if(a[i]>a[j]):
                a[i], a[j] = a[j], a[i]
                result += 1
    resultList.append([p+1,result])    
    
for i in resultList:
    print(i[0], i[1])