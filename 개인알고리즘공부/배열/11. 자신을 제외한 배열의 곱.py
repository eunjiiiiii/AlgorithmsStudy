"""
 배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라.

 ** 주의
 나눗셈을 하지 않고 O(n)에 풀이하라.
"""

nums = list(map(int, input().split())) # ex) [1,2,3,4]
res = []

# 왼쪽에서 곱한 리스트
p = 1

for i in range(len(nums)):
    res.append(p)
    p = nums[i] * p

p = 1
for i in range(len(nums)-1, 0 - 1, -1):
    res[i] = res[i] * p
    p = nums[i] * p

print(res)