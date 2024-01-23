# 실패율 구하는 함수
def calc_failure_rate(stop, reach, N):
    res = [0] * (N+1)  # 스테이지 별로 실패율 저장
    for i in range(1, N+1):
        try:
            res[i] = stop[i] / reach[i]
        except:  # 스테이지에 도달한 유저가 없는 경우(divisionByZero error이 발생)
            res[i] = 0  # 실패율은 9
    return res

def solution(N, stages):
    answer = []
    reach = [0] * (N+1)  # 각 스테이지에 도달한 인원 수 저장
    stop = [0] * (N+1)  # 각 스테이지에 멈춰있는 인원 수 저장
    for s in stages:
        if s > N:  # 모두 클리어한 사용자인 경우
            for i in range(1, s):
                reach[i] += 1
        else:
            stop[s] += 1  # 멈춰있는 스테이지 인원수 증가
            for i in range(1, s+1):
                reach[i] += 1  # 도달한 스테이지 인원수 증가
    
    
    rate = calc_failure_rate(stop, reach, N)
    rate = sorted(enumerate(rate), key=lambda x: (-x[1], x[0]))  # 실패율 정렬
    
    for idx, val in rate:
        if idx == 0:
            continue
        else:
            answer.append(idx)
        
    return answer