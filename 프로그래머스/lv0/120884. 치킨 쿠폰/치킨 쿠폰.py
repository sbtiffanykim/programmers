def solution(chicken):
    coupons = chicken
    answer = 0
    while coupons > 9:
        num_of_chicken = coupons // 10
        answer += num_of_chicken
        coupons %= 10
        coupons += num_of_chicken
        
    return answer