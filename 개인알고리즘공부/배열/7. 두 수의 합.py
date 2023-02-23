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

def twoSum_dict(nums, target):
    """
    in 연산자가 아닌 딕셔너리 이용해서 한번에 조회
    :param nums:
    :param target:
    :return:
    """

    num_dict = {}

    for i, num in enumerate(nums):
        num_dict[num] = i

    for i , num in enumerate(nums):
        if target - num in num_dict and num_dict[target - num] != i:
            return [i, num_dict[target- num]]


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    #print(twoSum_in(nums, target))
    print(twoSum_dict(nums, target))

    '''
    ex_dict = {'one':1, 'two': 2}
    if 1 in ex_dict:
        print(True)
    '''