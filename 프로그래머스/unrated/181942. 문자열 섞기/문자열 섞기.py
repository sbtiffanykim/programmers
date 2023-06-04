def solution(str1, str2):
    string = [c[0]+c[1] for c in zip(str1, str2)]
    return ''.join(string)