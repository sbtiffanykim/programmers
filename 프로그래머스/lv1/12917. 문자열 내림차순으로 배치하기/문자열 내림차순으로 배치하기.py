def solution(s):
    answer = ''
    
    ascii_nums = [ord(c) for c in s]
    ascii_nums.sort(reverse=True)
    answer = ''.join([chr(num) for num in ascii_nums])
    
    return answer