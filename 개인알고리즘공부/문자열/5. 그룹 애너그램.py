import collections

def groupAnagram(input_list):
    """
    문자열 배열을 받아 애너그램 단위로 그루핑하라.
    :param input_list: 문자열 배열
    :return: 애너그램 단위로 그루핑한 리스트
    """

    # 문제 접근 방향
    # 1. 예쁘게 정렬한 단어를 key로 딕셔너리 생성
    # 2. 정렬한 단어 key에 원래 단어를 리스트로 value 추가하기

    # 1. 예쁘게 정렬한 단어를 key로 딕셔너리 생성
    res = collections.defaultdict(list)
    for word in input_list:
        res[''.join(sorted(word))].append(word) # sorted(문자열) 결과는 항상 **리스트** 인걸 잊지 말기!!!!!!!!!!!!! -> 다시 문자열로 바꾸려면 ''.join()으로 감싸줘야함.

    return res

if __name__ == "__main__":
    input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # 3. **그루핑한 결과만** 출력하고 싶으므로 딕셔너리.values() (s랑 () 붙여야 함 !!!!!!!!!!) 해주기.
    print(list(groupAnagram(input_list).values()))