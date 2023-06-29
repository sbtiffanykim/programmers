def solution(t, p):
    answer = 0
    len_p = len(p)
    
    idx = 0
    while True:
        num = int(t[idx:idx+len_p])
        if int(p) >= num:
            answer += 1
        idx += 1
        if idx+len_p > len(t):
            break
    return answer