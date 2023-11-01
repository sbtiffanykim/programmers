def solution(n,a,b):
    answer = 1
    num = sorted([a, b])
    
    while True:
        # 번호 차이가 1이고, 작은 수가 홀수, 큰 수가 짝수여야 같은 라운드에서 붙음
        if num[1] - num[0] == 1 and num[0] % 2 != 0 and num[1] % 2 == 0:
            break        
        # 홀수번 번호는 짝수로 바꾸기
        num = list(map(lambda x: x + 1 if x % 2 != 0 else x, num))
        # 윗 라운드로 진출
        num = list(map(lambda x: x // 2 if x != 1 else 1, num))
        answer += 1
    return answer