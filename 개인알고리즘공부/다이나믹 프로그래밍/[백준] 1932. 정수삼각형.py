n = int(input())
dp = []

for i in range(n):
    dp.append(list(map(int, input().split())))


for i in range(1, n):
    for j in range(0, i+1):
        if j == 0:  # 각 라인의 처음은
            dp[i][0] += dp[i-1][0]  # 바로 위의 숫자를 더해주기
        elif j == i:    # 각 라인의 마지막은
            dp[i][j] += dp[i-1][j-1]    # 바로 위의 숫자를 더해주기
        else:   # 각 라인의 처음과 끝이 아닌 경우에는
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])   # 왼쪽 or 오른쪽 대각선 중 최대값을 더하기

print(max(dp[n-1])) # n-1행(가장 마지막 행)에서의 최댓값 출력

