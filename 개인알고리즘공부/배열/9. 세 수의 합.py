nums = list(map(int, input().split()))

# 투 포인터 이용
## 브루트포스로 할 경우 타임오버 발생하므로

# 0. 결과 담을 리스트 선언
res = []

# 1. 리스트 sort하기
nums.sort() # sort의 반환값은 None임. 이를 다시 어떠한 객체나 변수로 받을 생각 X

# 2. i 정하기
for i in range(len(nums)):
    # 중복된 값 건너 뛰기
    if i > 0 and nums[i] == nums[i - 1]:
        continue

    # 3. left, right 포인터 지정
    left, right = i+1, len(nums) - 1

    # 4. 투 포인터 구현
    while left < right:
        sum = nums[i] + nums[left] + nums[right]

        # 5. left, right 움직일 조건 설정
        if sum < 0 : # 정렬되어 있으니 더 큰수를 더하자
            left += 1
        elif sum > 0 :
            right -= 1
        else: # sum이 0이면
            res.append([nums[i], nums[left], nums[right]])

            # 6. left, right에서도 중복된 값 처리
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1

            left += 1
            right -= 1

print(res)

