from collections import deque

# 1. 입력 받기
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input()))) # nxm 2차원 배열로 받기
    
# 2. 상하좌우 방향 설정하기
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 3. 벽을 깼는지 여부를 나타내는 3차원 배열 만들기
#    벽을 깼을 때(c=1)의 경로와 벽을 깨지 않았을 때(c=0)의 경로로 나눠서 비교하려고
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1  # graph[0,0]은 조회했다고 1 넣어 주고 시작

def bfs(x, y, z):  # 시작 좌표를 매개변수로 받아 옴
    queue = deque()
    queue.append((x,y,z)) # queue에 저장할 값은 튜플로 관리!(좌표이므로)

    while queue: # queue가 비기 전까지
        a,b,c = queue.popleft()  # 1. queue pop 사용!!!!!

        # 2. 끝 좌표인지 check
        if a == n-1 and b == m-1:
            return visited[a][b][c] # 정상적인 처리 시 빠져나가는 루트

        # 3. 상하좌우 이동 : nx, ny 설정
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            # 4. nx, ny 좌표 유효 여부 check
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 5. 진짜 처리
            # 1) 다음에 이동할 곳이 벽이고, 아직 한번도 깨부신적이 없다면
            if graph[nx][ny] == 1 and c == 0:
                visited[nx][ny][1] = visited[a][b][0] + 1 # c=1로 새로 이동한 칸에 칸수 저장
                queue.append((nx, ny, 1)) # c = 1
            # 2) 다음에 이동할 곳이 벽이 아니고, 아직 한번도 방문하지 않은 곳이면
            elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                visited[nx][ny][c] = visited[a][b][c] + 1
                queue.append((nx, ny, c))

    return -1 # 비정상적인 처리 시 빠져나가는 루트

print(bfs(0,0,0))