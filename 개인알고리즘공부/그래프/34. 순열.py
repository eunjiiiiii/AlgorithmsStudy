import itertools

def permute(self, nums):
    """
    DFS 사용
    :param self:
    :param nums:
    :return:
    """
    results = []
    prev_elements = []

    def dfs(elements):
        # 리프 노드일 떄 결과 추가
        if len(elements) == 0:
            results.append(prev_elements[:])

        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()

    dfs(nums)
    return results

def permute_2(self, nums):
    return list(map(list, itertools.permutations(nums)))