from fractions import Fraction

answer = 0

def cal_slope(x, y):
    return Fraction((x[1]-y[1])/(x[0]-y[0]))

def solution(dots):
    dots.sort(key=lambda x:x[0])
    #12
    if cal_slope(dots[0], dots[1]) == cal_slope(dots[2], dots[3]):
        return 1
    #13
    elif cal_slope(dots[0], dots[2]) == cal_slope(dots[1], dots[3]):
        return 1    
    #14
    elif cal_slope(dots[0], dots[3]) == cal_slope(dots[1], dots[2]):
        return 1     
    
    return answer