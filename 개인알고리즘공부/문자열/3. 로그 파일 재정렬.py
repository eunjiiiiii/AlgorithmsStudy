def logResort(log_list):
    """
    리스트 타입의 로그가 주어졌을 때 재정렬해서 출력해주는 함수
    :param log_list: 입력 로그 리스트
    :return: 재정렬한 로그 리스트
    """

    digits = []
    letters = []

    # 1. 문자인 로그와 숫자인 로그 분리하기
    for log in log_list:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    # 2. 로그 재정렬하기 - lambda 이용
    letters.sort(key=lambda x: (x.split()[1], x.split()[0]))

    return letters + digits

if __name__ == "__main__":
    log_list = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    print(logResort(log_list))
