from collections import deque


def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    q1sum = sum(queue1)
    q2sum = sum(queue2)

    if (q1sum + q2sum) % 2 == 1:
        return -1

    # 이동 최대 limit 지정
    limit = len(queue1) + len(queue2)
    cnt = 0

    while q1sum != q2sum:
        if cnt >= limit:
            return -1

        # queue1 돌기
        while queue1 and q1sum > q2sum:
            # 합이 큰 큐에서 원소 삭제
            # 합이 작은 큐에 원소 추가
            tmp = queue1.popleft()
            queue2.append(tmp)
            cnt += 1
            q1sum -= tmp
            q2sum += tmp

        # queue2 돌기
        while queue2 and q1sum < q2sum:
            # 합이 큰 큐에서 원소 삭제
            # 합이 작은 큐에 원소 추가
            tmp = queue2.popleft()
            queue1.append(tmp)
            cnt += 1
            q2sum -= tmp
            q1sum += tmp
    return cnt


