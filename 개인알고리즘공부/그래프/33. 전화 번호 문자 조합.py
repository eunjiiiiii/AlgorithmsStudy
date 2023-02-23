def letterCombinations(self, digit: str):
    """
    2에서 9까지 숫자가 주어졌을 때 전화 번호로 조합 가능한 모든 문자를 출력하라.
    :param digit: # ex) "23"
    :return:
    """
    def dfs(index, path):
        if len(path) == len(digit):
            res.append(path)
            return

        for i in range(index, len(digit)):
            for j in dict[digit[i]]:
                dfs(i + 1, path + j)


    if not digit: # digit이 빈 리스트이면
        return []

    dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
           "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    res = []
    dfs(0, "")

    return res

    res = []