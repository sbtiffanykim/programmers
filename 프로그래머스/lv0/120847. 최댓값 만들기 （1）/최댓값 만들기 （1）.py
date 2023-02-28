def solution(numbers):
    m1_num = max(numbers)
    numbers.remove(m1_num)
    m2_num = max(numbers)
    
    answer = m1_num * m2_num
    return answer