def solution(num_list):
    odd_n = int(''.join([str(n) for n in num_list if n % 2 != 0]))
    even_n = int(''.join([str(n) for n in num_list if n % 2 == 0]))

    return odd_n + even_n