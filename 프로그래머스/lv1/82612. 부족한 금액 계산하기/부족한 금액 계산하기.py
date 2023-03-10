def solution(price, money, count):
    answer = money
    m_n = 0
    for i in range(1, count+1):
        m_n += (price * i)
    answer -= m_n
    if answer >= 0: answer = 0
    else: answer = abs(answer)
    return answer