'''
bin_value = list(input())
i = 0
oct_value = []
tmp = 0

bin_value.reverse()

if len(bin_value) % 3 != 0:
    bin_value.extend([0 for _ in range((len(bin_value) % 3)-1)])

while True:
    if i >= len(bin_value):  # while 탈출 조건
        break
      # 오른쪽부터 세개씩 자를 것이므로 인덱싱 편하게 reverse로 뒤집음
    if i % 3 == 0:  # index : 0, 3, 6, ...
        tmp += int(bin_value[i])  # 뒤집었으므로 세개의 숫자 중 가장 왼쪽에 있는 숫자에 1을 곱한다.
    elif i % 3 == 1:  # index : 1, 4, 7, ...
        tmp += int(bin_value[i]) * 2
    else:  # index : 2, 5, 8
        tmp += int(bin_value[i]) * 4
        oct_value.append(tmp)  # 뒤집었으므로 세개의 숫자 중 가장 오른쪽에 있는 숫자에 4을 곱한다.
        tmp = 0
    i += 1

oct_value.reverse()
result = ''.join(str(s) for s in oct_value)
print(result)
'''

print(oct(int(input(),2))[2:])