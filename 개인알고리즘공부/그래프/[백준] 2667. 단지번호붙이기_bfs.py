from collections import deque
# 1. 입력 받기
n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

# 2. 동서남북 방향 정의하기
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(graph, x, y):
    n = len(graph)
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0 # 탐색 완료
    cnt = 1

    while queue:    # queue가 비기 전까지
        x, y = queue.popleft()
        # 동서남북 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # dfs 에서 continue 조건 뺴먹지 말기!!!!!한꺼번에 쓰면 안됨.
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0   # 다시 탐색 못하게 0으로 변경
                cnt += 1

    return cnt


num = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            num.append(bfs(graph, i, j))

print(len(num))
for i in sorted(num):
    print(i)