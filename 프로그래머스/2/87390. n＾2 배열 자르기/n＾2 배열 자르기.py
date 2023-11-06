def solution(n, left, right):
    answer = []

    for i in range(left, right + 1):
        # nxn에서 i가 있는 위치 구하기
        r, c = i // n, i % n
        start = r + 1
        if c > r:
            answer.append(start + (c - r))
        else:
            answer.append(start)

    return answer