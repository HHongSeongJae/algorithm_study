N, K = map(int, input().split())
mlist = []
for _ in range(N):
    country, gold, silver, bronze = map(int, input().split())
    mlist.append((country, gold, silver, bronze))

#정렬
mlist.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

#특정국가메달찾기
search = next(x for x in mlist if x[0] == K)

#출력
for rank, country in enumerate(mlist, start=1):
    if country[1:] == search[1:]:
        print(rank)
        break