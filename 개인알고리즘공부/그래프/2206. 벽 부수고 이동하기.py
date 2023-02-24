def dfs(i, j, map):
    path = 0  # 경로 저장하는 변수
    if i < 0 or i >= len(map) or \
        j < 0 or j >= len(map[0]) or \
        map[i][j] == 1:
            return  # 종료


    if map[i][j] == 0:
        # 이미 조회한 노드는 1로 바꿔주기
        map[i][j] = 1

        # 동서남북 조회
        dfs(i - 1, j)
        dfs(i + 1, j)
        dfs(i, j - 1)
        dfs(i, j + 1)

        path += 1

    return path

# map 크기 입력 받기
n, m = map(int, input().split())
# for문으로 map 입력 받기
map = []
for i in range(n):
    # 한 행의 원소들을 리스트로 한꺼번에 받기
    map.append(list(map(int,input())))  # map에 리스트를 한 행씩 저장하여 2차원 리스트 만들기


one_count = 0  # 1 깨부신 횟수
path_list = []  # 경로 경우 저장하는 리스트
# dfs 이용한 최단경로 구하는 프로그램 구현
for i in range(n):
    for j in range(m):
        # 1이면
        if map[i][j] == 1:
            path_list.append(dfs(i, j, map))
            if one_count > 1:  # 최대 1번만 깨부시는게 가능하므로
                print(-1)
            one_count += 1

print(min(path_list))

