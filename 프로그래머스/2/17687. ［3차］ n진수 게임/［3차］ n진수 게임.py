def solution(n, t, m, p):
    # 0~15까지 출력해야하는 숫자/문자
    converted = {n: c for n, c in zip(range(16), '0123456789ABCDEF')}
    # n진법으로 변환된 숫자를 변환하여 저장
    nums = '0'

    for i in range(1, m * (t + 1) + 1):
        temp = []  # i가 n진법으로 바뀐 후의 숫자를 임시로 저장할 리스트
        # n진법으로 변환
        while i != 0:
            temp.append(i % n)
            i //= n
        # 변환된 수를 nums에 저장
        nums += ''.join([converted[t] for t in temp][::-1])

    # nums[p-1::m] => 튜브가 말해야하는 숫자
    # nums[p-1::m][:t] => 그 중 t개
    return nums[p - 1 :: m][:t]