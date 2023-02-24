from collections import deque

# 1. 입력 받기
r, c = map(int, input().split())

graph = []
for i in range(r):
    graph.append(list(input()))

# 2. BFS로 해결 # 왜인진 모르겠음...
def bfs(x,y):
    # 1. queue 선언
    queue = deque()
    queue.append((x,y))

    sheep, wolf = 0, 0
    # 초기조건도 양인지 늑대인지 check 하기!!!!!
    if graph[x][y] == 'o':
        sheep += 1
    elif graph[x][y] == 'v':
        wolf += 1
    graph[x][y] = '#'   # 조회했으니 울타리 '#'로 바꿔주기.(다시 검사 못하게)

    while queue: # 2. queue가 빌 때까지
        a,b = queue.popleft()

        # 3. 상하좌우 설정
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]

        ''' 
        # 4. 끝날 조건 check - # 끝날 조건 처리해줄 필요가 없음.
        if a == r-1 and b == c-1:
            return [graph[a][b][0], graph[a][b][1]]
        '''
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            '''
            # 5. nx, ny 조건 check - 예제 풀이에서는 continue 안쓰고 해당하는 조건에서 바로 조건 처리함.
            if nx < 0 or nx >= r-1 or ny < 0 or ny >= c-1:
                continue
            '''

            # 6. 실제 조건 처리
            # 현재 칸이 양이나 늑대인지 check하고 해당되면 개수 1 증가시키기
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != '#':
                if graph[nx][ny] == 'o':
                    # 양이면
                    sheep += 1
                elif graph[nx][ny] == 'v':
                    # 늑대이면
                    wolf += 1

                # count(=조회) 하고 나면 조회했다는 표시로 '#'로 값 변경해줌.
                graph[nx][ny] = '#'
                queue.append((nx, ny))

    # while문 끝나고 한 영역에 대한 반환값을 양의 마릿수와 늑대의 마릿수로 주기 위해 구현
    if wolf >= sheep:
        # 한 영역에 늑대의 수가 더 많으면
        return 0, wolf # 양은 없어짐
    elif sheep > wolf:
        # 한 영역에 양의 수가 더 많으면
        return sheep, 0 # 늑대를 물리침

sum_sheep, sum_wolf = 0, 0

for i in range(r):
    for j in range(c):
        if graph[i][j] in 'ov':
            sheep, wolf = bfs(i,j)
            sum_sheep += sheep
            sum_wolf += wolf

print(sum_sheep, sum_wolf)