def solution(a, b):
    days_past = 0
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = {0: 'FRI', 1: 'SAT', 2: 'SUN', 3: 'MON', 4: 'TUE', 5: 'WED', 6: 'THU'}
    
    if a != 1:
        for i in range(1, a):
            days_past += months[i-1]
    days_past += b - 1
        
    return days[days_past % 7]