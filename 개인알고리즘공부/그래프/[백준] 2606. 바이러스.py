import collections
# 1. 입력 받기
n = int(input())    # 컴퓨터의 수
pair_num = int(input()) # 쌍의 수

graph = collections.defaultdict(list)

for _ in range(pair_num):
    v, w = map(int,input().split())
    graph[v].append(w)
    graph[w].append(v)


def dfs(v, visited = []):
    visited.append(v)
    for w in graph[v]:
        if w not in visited:
            visited = dfs(w, visited)
    return visited

print(len(dfs(1)) - 1)