import re

def solution(polynomial):
    answer = ''
    eq = list(polynomial.replace('+', ' ').split(' '))
    coeff, const = 0, 0
    for e in eq:
        if e.isnumeric(): const += int(e)
        elif e.isnumeric() == 0 and len(e) > 0:
            if len(e) == 1: coeff += 1
            else:
                coeff += int(e[:-1])

    if coeff == 0 and const == 0: return '0'
    if coeff == 1: coeff = ''
    if coeff == 0: return str(const)
    if const == 0: return str(coeff) + 'x'
    
    return str(coeff) + 'x + ' + str(const)