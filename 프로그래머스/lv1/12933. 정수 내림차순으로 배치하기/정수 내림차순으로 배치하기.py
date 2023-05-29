def solution(n):
    num_list = []
    while n >= 1:
        num_list.append(str(n % 10))
        n //= 10
        
    num_list.sort(reverse=True)
    return int(''.join(num_list))