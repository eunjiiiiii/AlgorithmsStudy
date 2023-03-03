# 조합 문제!!!!!!!
# dfs 나 itertools 이용해서 풀기
# -> 아님. bfs 문제임.
# bfs로 완전탐색 구현하는 문제. visited로 경우의 수 구해서 하기.

# 1. 입력받기
a,b,c = map(int, input().split())

visited = [[0]*(b+1) for _ in range(a+1)] #


# 2. 경우의 수 기록하는 함수 만들기
def pour(x, y):
    if not visited[x][y]:
        visted[x][y] = 1
        queue.append((x,y))

