def solution(numbers, hand):
    # numbers : 순서대로 누를 번호
    # hand : 오른손잡이 or 왼손잡이
    answer = ''
    # key_pad: 키패드 숫자 담은 이차원 배열
    # key_pad = [[ i+1 for i in range(i*3,i*3+3)] for i in range(3)]
    key_pad = [i + 1 for i in range(9)] + ['*', 0, '#']
    print(key_pad)
    # key_pad.index(4)
    r_idx = key_pad.index('#')  # 현재 오른손 위치
    l_idx = key_pad.index('*')  # 현재 왼손 위치

    for n in numbers:  # 탐색해야 할 숫자
        n_idx = key_pad.index(n)
        print('*' * 10)
        print('n: ', n, ' n_idx: ', n_idx)
        print('l_idx = ', l_idx, ' r_idx = ', r_idx)
        if n_idx % 3 == 0:  # 왼손으로 칠 수 있는 숫자일 경우
            answer += 'L'
            l_idx = n_idx  # 현재 왼손이 위치한 숫자
        elif n_idx % 3 == 2:  # 오른손으로 칠 수 있는 숫자일 경우
            answer += 'R'
            r_idx = n_idx  # 현재 오른손이 위치한 숫자
        else:  # 가운데 있는 숫자일 경우
            print('n_idx - l_idx = ', abs(n_idx - l_idx), ' n_idx - r_idx = ', abs(n_idx - r_idx))
            if abs(n_idx - l_idx) > abs(n_idx - r_idx):  # r_num이 더 가까울 때
                answer += 'R'
                r_idx = n_idx
            elif abs(n_idx - l_idx) < abs(n_idx - r_idx):  # r_num이 더 가까울 때
                answer += 'L'
                l_idx = n_idx
            else:  # 같을 경우
                answer += hand[0].upper()
                print('hand[0]', hand[0])
                if hand[0] == 'r':
                    r_idx = n_idx
                else:
                    l_idx = n_idx
    return answer

# [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], right -> "LRLLLRLLRRL"
# 1,4,7 index : 0,3,6,9
# 3,6,9 index : 2,5,8,11