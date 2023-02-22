def isPalindrom_list(s:str) -> bool:
    """
    입력 받은 문자열이 펠린드롬인지 판별하는 함수 - 1. 리스트 이용
    대소문자 상관 없고, 영문자와 숫자만 판별에 사용한다.
    :param s: 입력 문자열
    :return: True or False
    """

    # 1. 문자열 전처리
    #    대소문자 -> 소문자로 통일, 영문자나 숫자가 아닌 문자들은 지우기

    processed_str = []

    for char in s:
        if char.isalnum(): # True이면
            processed_str.append(char.lower()) # 소문자로 변경 후 리스트에 원소로 추가하기

    # 2. 펠린드롬 여부 체크
    while len(processed_str) > 1:
        if processed_str.pop(0) != processed_str.pop():
            # 양 끝을 비교했을 때 같지 않으면 (pop 연산을 씀으로써 비교와 함께 원소 삭제까지)
            return False

    return True










import collections

def isPalindrom_deque(s: str) -> bool:
    """
    입력 받은 문자열이 펠린드롬인지 판별하는 함수 - 2. 덱 이용
    대소문자 상관 없고, 영문자와 숫자만 판별에 사용한다.
    :param s: 입력 문자열
    :return: True or False
    """

    # 리스트 대신 덱으로 정의!
    processed_str: Deque = collections.deque()

    # 1. 전처리
    for char in s:
        if char.isalnum(): # 알파벳이나 숫자이면
            processed_str.append(char.lower())

    # 2. 펠린드롬 체크
    while len(processed_str) > 1:
        if processed_str.popleft() != processed_str.pop():
            return False
    return True

def isPalindrom_deque(s: str) -> bool:
    """
    덱 이용 - 복습
    :param s: 입력 문자열
    :return: True or False
    """

    # 데크 변수 객체 선언
    processed_str: Deque = collections.deque()

    # 문자열 전처리 - 영문자, 숫자 제외 삭제
    for char in s:
        if char.isalnum():
            processed_str.append(char.lower())

    # 펠린드롬 체크
    while len(processed_str) > 1: # 1로 설정하는 이유는 가운데 문자가 하나 남고 나머지가 다 대칭이어도 펠린드롬임
        if processed_str.popleft() != processed_str.pop():
            return False
    return True

import re

def isPalindrom_slicing(s:str) -> bool:
    """
    3. 문자열 슬라이싱 이용
    :param s: 입력 문자열
    :return: True or False
    """

    # 정규식을 이용한 문자열 전처리
    s = s.lower() # 소문자로 먼저 다 바꿔주기. lower는 inplace 안되므로 다시 변수에 집어넣는 과정 해줘야함.
    s = re.sub('[^a-z0-9]', '', s) # 영문자와 숫자가 아니면(^) ''로 대체

    return s == s[::-1]


if __name__ == "__main__":

    s = input()
    #print(isPalindrom_list(s))
    #print(isPalindrom_deque(s))
    print(isPalindrom_slicing(s))