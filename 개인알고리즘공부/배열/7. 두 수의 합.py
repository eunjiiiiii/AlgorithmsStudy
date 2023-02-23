def twoSum_in(nums, target):
    """
    브루트포스가 아닌 in 연산자 이용해서 복잡도 감소
    :param nums:
    :param target:
    :return:
    """

    for i, num in enumerate(nums):
        rest = target - num

        if rest in nums[i+1:]:
            print(nums[i + 1:].index(rest))

            return [nums.index(num), nums[i+1:].index(rest) + (i+1)]


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    print(twoSum_in(nums, target))