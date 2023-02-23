import sys

while True:
    strings = sys.stdin.readline().rstrip('\n')

    if not strings:
        break

    # 소문자, 대문자, 숫자, 공백
    l, u, d, s = 0, 0, 0, 0
    for string in strings:
        if string.islower(): # 소문자 count
            l += 1
        elif string.isupper(): # 대문자 count
            u += 1
        elif string.isdigit(): # 숫자 count
            d += 1
        elif string.isspace(): # 공백 count
            s += 1

    print(l, u, d, s)