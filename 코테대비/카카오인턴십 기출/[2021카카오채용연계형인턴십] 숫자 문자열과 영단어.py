def solution(s):
    answer = 0
    str_int_dict = {'one': '1', 'two': '2', 'three': '3',
                    'four': '4', 'five': '5', 'six': '6',
                    'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0'}

    for k, v in str_int_dict.items():
        s = s.replace(k, v)

    return int(s)