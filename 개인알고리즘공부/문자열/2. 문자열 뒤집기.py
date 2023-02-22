def reverseString(s: str) -> None:
    """
    문자열 뒤집기 - 1. 투 포인터 사용
    :param s: 입력 문자열
    :return: 뒤집어진 문자열
    """

    #tmp_char = ''
    str = list(s)
    # 1. 투 포인터 선언
    left, right = 0, len(str) - 1

    # 2. 문자열 뒤집기
    while left < right:
        str[left], str[right] = str[right], str[left]
        left += 1
        right -= 1
    print(str)

def reverseString_slicing(s:str) -> None:

    str = list(s)
    str.reverse()
    print(str)

if __name__ == "__main__":
    s = input()
    #reverseString(s)
    reverseString_slicing(s)