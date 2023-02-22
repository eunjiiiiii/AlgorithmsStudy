def mostLongPalindrom(s: str) -> str:
    """
    주어진 문자열에서 가장 긴 팰린드롬 부분 문자열 찾기
    :param s: 주어진 문자열
    :return: 가장 긴 팰린드롬 부분 문자열
    """

    # 문제 접근 방향
    # 1. 투 윈도우 이용(짝수 윈도우, 홀수 윈도우)
    # 2. 두 윈도우로 문자열 끝까지 탐색하면서 팰린드롬 찾으면 확장해나가면서 검사하기

    # 1. 투 윈도우 이용(짝수 윈도우, 홀수 윈도우) - 함수 만들어주기
    def expand(left: int, right: int, s: str):
        """
        윈도우의 시작과 끝 포인터가 주어졌을 떄 이를 확장해 나가는 함수
        :param left: 윈도우 시작 포인터
        :param right: 윈도우 끝 포인터
        :return: 문자열
        """

        while left >= 0 and right < len(s) \
                and s[left] == s[right]: # right는 인덱스니까
            left -= 1
            right += 1

        return s[left + 1: right] # 그 이전까지니까 left에는 1 더해주고, right는 그대로 놔두기(어차피 인덱싱 룰이 그러므로)

    # 2. 문자열 길이가 1이거나, 문자열 전체가 팰린드롬인거 제외
    if len(s) < 2 or s == s[::-1]:
        return s

    res = ''
    for i in range(len(s) - 1):
        res = max(res,
                  expand(i, i+1, s),
                  expand(i, i+2, s),
                  key = len) # *********중요!!!!!!!!!!!!!!!!1

    return res

if __name__ == "__main__":
    s = input() # ex) "babad" / "cbbd"
    print(mostLongPalindrom(s)) # ex) "bab" / "bb"