from collections import deque

N, M, V = map(int,input().split())
graph = [[0] * (N+1) for _ in range(N+1)] # graph 초기화

for i in range(M):
    x, y = map(int, input().split())
    graph[x][y] = 1 # 입력받은 위치는 1로 바꿔주기
    graph[y][x] = 1

visited_dfs = [0] * (N+1) # dfs 방문 기록
visited_bfs = [0] * (N+1) # bfs 방문 기록

def bfs(v):
    queue = deque([v])
    visited_bfs[v] = 1 # 방문한 v위치에 1값 넣기
    while queue: # queue를 다 돌때까지
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, N+1): # 1부터 N까지 돌면서
            if visited_bfs[i] == 0 and graph[v][i] == 1: # 아직 방문하지 않은 곳이라면
                queue.append(i) # 해당 위치 추가
                visited_bfs[i] = 1 # 그리고 방문했다는 표시로 1값 넣어주기

def dfs(v):
    visited_dfs[v] = 1 # 먼저 방문했다는 표시로 1 넣어주기
    print(v, end=' ')
    for i in range(1, N+1):
        if visited_dfs[i] == 0 and graph[v][i] == 1:
            dfs(i) # 재귀로 깊이 탐색


dfs(V)
print()
bfs(V)

