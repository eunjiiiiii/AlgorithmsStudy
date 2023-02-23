def arrayPartition_pair1(nums) -> int:
    """
    1. 오름차순 정렬한 후 pair 만들어서  min 구해서 더하는 방법
    :param nums:
    :return:
    """
    sum_res = 0
    pair = []
    nums.sort() # sort는 반환값이 None이므로 sort하고 다른 변수나 객체에 받지 않도록 한다.

    for num in nums:
        pair.append(num)
        if len(pair) == 2:
            sum_res += min(pair)
            pair = []

    return sum_res

def arrayPartition_pair2(nums) -> int:
    """
    어차피 정렬하면 min은 짝수인덱스에 위치
    :param nums:
    :return:
    """
    sum_res = 0
    nums.sort() # 오름차순으로 정렬

    for i, num in enumerate(nums):
        if i % 2 == 0: # 짝수번째 인덱스이면
            sum_res += num

    return sum_res

def arrayPartition_pair3(nums) -> int:
    """
    파이썬의 문법을 살려서 푸는 방법 - 슬라이싱!!
    :param nums:
    :return:
    """
    return sum(sorted(nums)[::2]) # ::2 는 두 칸마다 건너 뛴 리스트 반환
    # .sort() 안되면 sorted()이용하기!!!!!!!!!!!!!!!!!!!

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    #print(arrayPartition_pair1(nums))
    #print(arrayPartition_pair2(nums))
    print(arrayPartition_pair3(nums))

