def numIsland(grid) -> int:
    """
    1이 육지, 0이 바다를 뜻할 때, 섬의 개수를 반환하는 함수
    :param input_list: 리스트이지만 그래프로 인식하기
    :return:
    """


    def dfs(i, j):
        if (i < 0 or i>=len(grid)) or(j < 0 or j >= len(grid[0])) or (grid[i][j] != '1'):
            return # 종료

        grid[i][j] = 0 # 여기로 넘어왔다는 뜻은 육지라는 뜻이므로(== grid[i][j] == '1') 검사한 좌표는 0으로 바꾸기

        dfs(i,j-1) # 서
        dfs(i,j+1) # 동
        dfs(i-1, j) # 북
        dfs(i+1, j) # 남

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1

    return count



if __name__ == "__main__":
    grid = [[1,1,1,1,0],
                  [1,1,0,1,0],
                  [1,1,0,0,0],
                  [0,0,0,0,0]]

    print(numIsland(grid))

