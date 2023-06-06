def solution(num, total):
    answer = []
    mid_num = total // num
    
    if num % 2 == 0:
        idx_of_mid_num = num // 2 - 1
    else:
        idx_of_mid_num = num // 2
    
    for i in range(num - idx_of_mid_num):
        answer.append(mid_num + i)
    for i in range(1, idx_of_mid_num+1):
        answer.append(mid_num - i)
        
    answer.sort()
    return answer