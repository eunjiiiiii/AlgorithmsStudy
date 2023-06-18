'''
def solution(arr):
    cnt = 0
    tmp = -1    # tmp 초기화
    answer = []
    for element in arr:
        if tmp == element:
            cnt += 1   #중복 횟수 세기
        else:
            # 중복되지 않으면
            if cnt > 0:
                answer.append(cnt)  #정답 리스트에 추가
            cnt = 0 # cnt 초기화
        tmp = element   # tmp 초기화

    return answer
'''

import collections

def solution(arr):
    answer = []
    count_dict = collections.Counter(arr)
    for key, value in count_dict.items():
        if value > 1: # 중복된게 있으면
            answer.append(value)

    return answer



if __name__ == "__main__":
    arr = [1,2,3,3,3,4,4]
    print(solution(arr))
