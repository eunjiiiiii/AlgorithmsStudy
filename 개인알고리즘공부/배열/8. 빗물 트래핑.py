def rainTrapping(height) -> int:
    """
    투 포인터 이용
    :param input_list: 각 x 좌표에 대한 y 좌표(높이)
    :return: 빗물 찬 칸의 수
    """

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    volume = 0

    while left < right:
        left_max = max(left_max, height[left])
        right_max = max(right_max, height[right])

        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1

    return volume

if __name__ == "__main__":
    input_list = list(map(int, input().split()))
    print(rainTrapping(input_list))
