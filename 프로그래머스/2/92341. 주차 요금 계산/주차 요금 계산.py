import math
from collections import defaultdict


def calc_fee(m, fees):
    price = fees[1]  # 기본요금
    if m > fees[0]:
        price += math.ceil((m - fees[0]) / fees[2]) * fees[3]
    return price


def solution(fees, records):
    answer = []

    # 입력
    new_status = defaultdict(str)  # {차량번호: [상태, 현재시간, 누적시간]}
    for r in records:
        time, car_num, status = r.split(' ')
        h, m = map(int, time.split(':'))
        curr_time = h * 60 + m  # 현재 시간을 분으로 바꿈
        if status == 'IN':
            # 그 전 기록이 없으면 새로 입력
            if car_num not in new_status:
                new_status[car_num] = [1, curr_time, 0]
            # 아니라면 상태, 현재시간만 갱신
            else:
                new_status[car_num][1] = curr_time
                new_status[car_num][0] = 1
        elif status == 'OUT':
            # 누적시간 계산
            parking_time = curr_time - new_status[car_num][1]
            new_status[car_num][0] = 2
            new_status[car_num][1] = curr_time
            new_status[car_num][2] += parking_time

    price = defaultdict(str)
    for r in new_status:
        # 미출차 차량 누적시간 정리
        if new_status[r][0] == 1:
            new_status[r][2] += (23 * 60 + 59) - new_status[r][1]
        # 계산
        tmp = calc_fee(new_status[r][2], fees)
        price[r] = tmp
    # 차 번호 작은 순으로 정렬
    price = sorted(price.items(), key=lambda x: x[0])
    answer = [p for n, p in price]

    return answer