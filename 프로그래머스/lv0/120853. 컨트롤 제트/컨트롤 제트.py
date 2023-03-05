def solution(s):
    answer = 0
    s_list = s.split(' ')
    prev_n = int(s_list[0])
    answer += prev_n
    
    for char in s_list[1:]:
        try:
            num = int(char)
            answer += num
            prev_n = num
        # if a char is Z
        except ValueError:
            answer -= prev_n
    
    return answer