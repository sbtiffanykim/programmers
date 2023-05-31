def solution(s):
    answer = ''
    
    words = s.split(' ')
    for word in words:
        converted = [val.upper() if idx % 2 == 0 else val.lower() for idx, val in enumerate(word)]
        answer += ''.join(converted)
        answer += ' '
    
    answer = answer[:-1]
    
    return answer