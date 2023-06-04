def solution(a, b):
    first = int(str(a)+str(b))
    second = 2 * a * b
    return first if first >= second else second