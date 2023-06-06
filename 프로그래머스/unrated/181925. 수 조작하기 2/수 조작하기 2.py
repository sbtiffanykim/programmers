def solution(numLog):
    answer = ''
    controls = {1: 'w', -1: 's', 10: 'd', -10: 'a'}
    prev_num = numLog[0]
    for num in numLog[1:]:
        answer += controls[num-prev_num]
        prev_num = num
    return answer