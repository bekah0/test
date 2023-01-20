from collections import deque

import sys

input=sys.stdin.readline


for i in range(int(input())) :
    n,k=map(int,input().split())
    q=deque(list(map(int,input().split())))

    for j in range(len(q)) :
        q[j]=(q[j],j)

    dp=[0]*n
    c=0
    while q :
        if q[0][0] == max(q)[0] :
            dp[q[0][1]]=c
            q.popleft()
            c+=1
        else:
            q.append(q.popleft())

    print(dp[k]+1)