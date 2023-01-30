from collections import deque
import sys
input=sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    deq=deque()
    deq.append([x,y])
    visit[x][y]=1
    check=1

    while deq:
        x,y=deq.popleft()

        for i in range(4):
            nx=x+dx[i] ; ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and not visit[nx][ny] and graph[nx][ny]==1:
                visit[nx][ny]=1
                check+=1
                deq.append([nx,ny])

    return check  

n,m=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
visit=[[0]*m for _ in range(n)]
count=0 ; tmp=0 

for i in range(n):
    for j in range(m):
        if graph[i][j]==1 and not visit[i][j]: 
            tmp=max(tmp , bfs(i,j) ) 
            count+=1 

print(count , tmp , sep='\n')