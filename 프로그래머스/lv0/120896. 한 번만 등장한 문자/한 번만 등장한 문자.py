def solution(s):
    answer = ''
    a = list(set(s))
    occr = []
    for char in a:
        if s.count(char) == 1:
            occr.append(char)
    occr.sort()
    if len(occr) == 0: return ''
    answer = ''.join(occr)
    return answer
