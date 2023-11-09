def solution(numbers, hand):
    answer = ''
    # key_pad: 키패드 숫자 담은 이차원 배열
    key_pad = [i + 1 for i in range(9)]
    key_pad += ['*', 0, '#']
    print(key_pad)

    pre_x = [key_pad.index('#') // 3, key_pad.index('*') // 3]  # [왼손 x, 오른손 x]
    pre_y = [key_pad.index('#') % 3, key_pad.index('*') % 3]  # [왼손 y, 오른손 y]

    for n in numbers:
        # x,y index
        n_idx = key_pad.index(n)
        now_x, now_y = divmod(n_idx, 3)

        # 1,4,7 / 3,6,9 구분
        if now_y == 0:  # 1,4,7
            answer += 'L'
        elif now_y == 2:  # 3,6,9
            answer += 'R'
        else:  # 2,5,8,0
            if abs(pre_x[0] - now_x) + abs(pre_y[0] - now_y) < abs(pre_x[1] - now_x) + abs(pre_y[1] - now_y):
                answer += 'L'
            elif abs(pre_x[0] - now_x) + abs(pre_y[0] - now_y) > abs(pre_x[1] - now_x) + abs(pre_y[1] - now_y):
                answer += 'R'
            else:  # 거리 같으면
                answer += hand[0].upper()

        if answer[-1] == 'L':
            pre_x[0] = now_x
            pre_y[0] = now_y
        else:
            pre_x[1] = now_x
            pre_y[1] = now_y

    return answer

# [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], right -> "LRLLLRLLRRL"
# 1,4,7 index : 0,3,6,9
# 3,6,9 index : 2,5,8,11