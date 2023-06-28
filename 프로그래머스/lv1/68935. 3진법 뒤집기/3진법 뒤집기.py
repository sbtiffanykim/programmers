def solution(n):
    rev_ter_num = ''

    if n == 1: rev_ter_num = '1'
    elif n == 2: rev_ter_num = '2'
    else:
        while n > 2:
            a, b = divmod(n, 3)
            n = a
            rev_ter_num += str(b)
        rev_ter_num += str(a)
    return int(rev_ter_num, 3)