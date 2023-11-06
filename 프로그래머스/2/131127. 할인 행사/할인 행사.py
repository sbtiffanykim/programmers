def solution(want, number, discount):
    answer = 0
    start = 0  # 시작 index
    while start + 10 <= len(discount):  # 시작 index로부터 10개까지 품목 확인
        products = discount[start : start + 10]
        if all([products.count(p) == num for p, num in zip(want, number)]):  # 원하는 종류와 개수가 모두 존재한다면
            answer += 1  # 정답 추가
        start += 1  # 시작 index 1칸 증가

    return answer