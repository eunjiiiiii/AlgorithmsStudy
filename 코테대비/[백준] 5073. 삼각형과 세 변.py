while True:
    num = [int(x) for x in input().split()] # 입력 받기
    num.sort()
    num = num[::-1]

    if sum(num) == 0:   # 0 0 0 입력 되면 종료
        break

    # 삼각형 세 변의 길이 비교
    # 1. Invalid : 삼각형의 조건을 만족하지 못하는 경우
    if 2 * num[0] >= sum(num):
        print("Invalid")

    # 2. Equilateral : 세 변의 길이가 모두 같은 경우
    elif num[0] == num[-1]:
        print("Equilateral")

    # 3. Isosceles : 두 변의 길이만 같은 경우
    elif num[0] == num[1] or num[1] == num[-1]:
        print("Isosceles")

    # 4. Scalene : 세 변의 길이가 모두 다른 경우
    else:
        print("Scalene")


