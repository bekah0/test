import sys

input=sys.stdin.readline

sys.setrecursionlimit(10**4)

dx=[-1,1,0,0]
dy=[0,0,-1,1] #상하좌우
#
def dfs(a,b) :
    global tot 
    tot += 1
    visit[a][b] = True

    for i in range(4) :
        x=a+dx[i]
        y=b+dy[i]

        if 0<=x<k and 0<=y<n and visit[x][y]==False and graph[x][y]==1 :
            
            dfs(x,y) 

k,n,q=map(int,input().split())
    
ans=0
graph=[[0]*n for _ in range(k)]

visit=[[False]*n for _ in range(k)]

for i in range(q) :
    a,b=map(int,input().split())
    graph[a-1][b-1]=1

for i in range(k) :
    for j in range(n) :
        if visit[i][j]==False and graph[i][j]==1 :
            #global tot
            tot=0
            dfs(i,j) 
            ans=max(ans,tot)


print(ans)
