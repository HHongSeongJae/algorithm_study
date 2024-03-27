import sys

n = int(input())

S = set()
for i in range(n):
    active = list(sys.stdin.readline().split())

    if active[0] == 'add':
        S.add(int(active[1]))
    elif active[0] == 'remove':
        S.discard(int(active[1]))
    elif active[0] == 'check':
        if int(active[1]) in S:
            print(1)
        else:
            print(0)
    elif active[0] == 'toggle':
        if int(active[1]) in S:
            S.discard(int(active[1]))
        else:
            S.add(int(active[1]))
    elif active[0] == 'all':
        for i in range(1,21):
            S.add(i)
    elif active[0] == 'empty':
        S = set()
