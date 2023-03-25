def solution(n):
    num_list = [0]
    for i in range(1, 300):
        if i % 3 == 0 or '3' in str(i):
            continue
        else:
            num_list.append(i)
    answer = num_list[n]
    return answer