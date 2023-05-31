def solution(price, money, count):
    need = sum([i * price for i in range(1, count+1)]) - money
    return need if need > 0 else 0