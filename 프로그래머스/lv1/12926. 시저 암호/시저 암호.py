def solution(s, n):
    answer = ''
    
    for c in s:
        if c == ' ': answer += ' '
        else:
            if c.isupper() and ord(c)+n not in range(ord('A'), ord('Z')+1): answer += chr(ord(c) + n - 26)
            elif c.islower() and ord(c)+n not in range(ord('a'), ord('z')+1): answer += chr(ord(c) + n - 26)
            else: answer += chr(ord(c) + n)
            
    
    return answer