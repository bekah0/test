import sys

input=sys.stdin.readline

sys.setrecursionlimit(10**5)

dx=[-1,1,0,0,1,1,-1,-1]
dy=[0,0,-1,1,1,-1,1,-1]

def dfs(a,b) :
    visit[a][b] = True

    for i in range(8) :
        x=a+dx[i]
        y=b+dy[i]

        if 0<=x<k and 0<=y<n and visit[x][y]==False and graph[x][y]==1 :
            dfs(x,y)

while True:
    n,k=map(int,input().split())
    if n==0 and k == 0 :
        break
    
    graph=[list(map(int,input().split()))for _ in range(k)]

    visit=[[False]*n for _ in range(k)]

    t=0
    for i in range(k) :
        for j in range(n) :
            if visit[i][j]==False and graph[i][j]==1 :
                t+=1
                dfs(i,j)

    print(t)
