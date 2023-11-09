import re

# 다소 복잡한 코드..

def solution(s):
    answer = 0
    str_int_dict = {'one': '1', 'two': '2', 'three': '3',
                    'four': '4', 'five': '5', 'six': '6',
                    'seven': '7', 'eight': '8', 'nine': '9'}

    str_list = re.findall(r'[a-z]+', s)

    for s_int in str_list:
        try:
            s = re.sub(s_int, str_int_dict[s_int], s)
        except:
            for k, v in str_int_dict.items():
                try:
                    if s.index(k) > -1:
                        s = s[: s.index(k) + len(k)] + ' ' + s[s.index(k) + len(k):]
                        s = re.sub(k, v, s)
                except:
                    pass

    return int(s.replace(' ', ''))