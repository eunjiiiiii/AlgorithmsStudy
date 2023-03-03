n = int(input())

graph = [list(map(int, input())) for _ in range(n)]


# 동서남북
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

cnt = 0
num = []
res = 0

def dfs(x, y):
    # 탈출 조건
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    # 문제 조건
    if graph[x][y] == 1:
        global cnt
        cnt += 1
        # 방문했다는 표시로 0 으로 업데이트
        graph[x][y] = 0

        # 동서남북 방문
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            dfs(nx, ny)
        return True
    return False

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            num.append(cnt)
            res += 1
            cnt = 0

print(res)
for k in sorted(num):
    print(k)