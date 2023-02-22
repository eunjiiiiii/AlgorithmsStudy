import re
import collections

def mostCommonChar(paragraph: str, banned) -> str:
    """
    주어진 문자열에서 구분자 상관하지 않고 대소문자 구분하지 않고
    금지된 단어를 제외하고 가장 흔한 단어 반환하기
    :param paragraph: 주어진 문자열
    :param banned: 금지된 단어 리스트
    :return: 가장 흔한 단어 문자열
    """

    # 1. 전처리
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() # re.sub('r[^\w]', , ) : 구분자 제거, lower() : 대소문자 구분 X, split() : 문자 하나하나 보기
             if word not in banned] # 문자 하나하나가 금지된 단어가 아니면 리스트에 원소로 추가하기

    """
    # 2. 가장 흔한 단어 찾기 - 1. Counter 이용
    res = collections.Counter(words)
    return res.most_common(1)[0][0]
    """

    # 2. 가장 흔한 단어 찾기 - 2. 직접 구현
    res = collections.defaultdict(int)
    for word in words:
        res[word] += 1 # word를 key로 딕셔너리에 count하기

    # 최대값 찾기
    return max(res, key=res.get)


if __name__ == "__main__":
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    print(mostCommonChar(paragraph, banned))