# 1. n, k 입력받기
n, k = map(int, input().split())

# 2. coin 종류 입력 받기
coins = []
for i in range(n):
    coins.append(int(input()))

# 3. dp 리스트 만들기
dp = [0] * (k+1)
dp[0] = 1

# 4. for문 통해서 경우의 수 누적 합 구하기
for c in coins: # coin 종류를 돌면서
    for j in range(c, k+1): # 앞에 탐색한 경우는 제외하고, 주어진 합에서 동전을 뺸 수가 양수이면
        # 즉, coin을 더 이용해서 합을 만들어야 할 경우이면
        p_case = dp[j - c]
        dp[j] += p_case

print(dp[k])    # 구하고자 하는 합의 경우의 수 출력하기





def merge(left, right):
    left_len = len(left)
    right_len = len(right)

    result = []
    left_idx = right_idx = 0

    while len(result) < left_len + right_len:
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

        if right_idx == right_len:
            result.extend(left[left_idx:])
            break
        if left_idx == left_len:
            result.extend(right[right_idx:])
            break

    return result


from random import randint

def quicksort(arr):
    if len(arr) < 2:
        return arr

    low, same, high = [], [], []
    pivot = arr[randint(0, len(arr)-1)]

    for item in arr:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    return quicksort(low) + same + quicksort(high)

