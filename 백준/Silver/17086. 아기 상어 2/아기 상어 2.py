from collections import deque
import sys
input=sys.stdin.readline

dx=[-1,1,0,0,-1,-1,1,1]
dy=[0,0,-1,1,-1,1,-1,1]

def bfs():
    while deq:
        x,y=deq.popleft()
        for i in range(8) :
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and not visit[nx][ny] and graph[nx][ny]==0 :
                visit[nx][ny]=visit[x][y]+1
                deq.append([nx,ny])


n,m=map(int,input().split())
graph=[list(map(int,input().split()))for _ in range(n)]
visit=[[0]*m for _ in range(n)]
deq=deque()
for i in range(n) :
    for j in range(m) :
        if graph[i][j]==1 :
            deq.append([i,j])
            visit[i][j]=1

bfs()

ans=0
for i in range(n) :
    for h in range(m) :
        ans=max(ans,visit[i][h]-1)

print(ans)