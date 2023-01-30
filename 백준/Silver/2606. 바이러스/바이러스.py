import sys
input=sys.stdin.readline

def dfs(node) :
    global count
    visit[node]=True
    for i in graph[node] :
        if not visit[i] :
            count += 1
            dfs(i)
n=int(input())
k=int(input())

graph=[ [] for _ in range(n+1)]
visit=[False]*(n+1)

for i in range(k) :
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


count = 0
dfs(1)

print(count)